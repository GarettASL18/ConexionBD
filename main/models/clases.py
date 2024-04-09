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
    def __init__(self, id=0, ciudad_id=None , jobs_id=None, name="", salario="", status=1):
        self.id = id
        self.jobs_id = jobs_id
        self.ciudad_id = ciudad_id
        self.name = name
        self.status = status
        self.salario = salario
        

    def __str__(self):
        return self.name
    