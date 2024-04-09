import mysql.connector

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None
        self.connect()

    def connect(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)

    def close(self):
        self.cnx.close()
    
    def execute_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        self.cnx.commit()
        cursor.close()
        return cursor
    
    def execute_read_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result
    
class DaoCity:
    def __init__(self, connection):
        self.connection = connection

    def get_all(self):
        query = 'SELECT * FROM cities'
        return self.connection.execute_read_query(query, ())

    def get_by_id(self, id):
        query = 'SELECT * FROM cities WHERE ciudad_id = %s'
        return self.connection.execute_read_query(query, (id))

    def insert(self, city):
        query = 'INSERT INTO cities (name, status) VALUES (%s, %s)'
        return self.connection.execute_query(query, (city.name, city.status))

    def update(self, city):
        query = 'UPDATE cities SET name = %s, status = %s WHERE ciudad_id = %s'
        return self.connection.execute_query(query, (city.name, city.status, city.id))

    def delete(self, id):
        query = 'DELETE FROM cities WHERE ciudad_id = %s'
        return self.connection.execute_query(query, (id))

    
