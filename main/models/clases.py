import mysql.connector

class City:
    def __init__(self, id =0, name="", status=1):
        self.id = id
        self.name = name
        self.status = status
        
    def __str__(self):
        return self.name
    
class Jobs:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def __str__(self):
        return self.name
    
class Employees:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def __str__(self):
        return self.name