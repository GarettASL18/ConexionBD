import os
from dao.daoConnection import Connection, DaoCity
from models.clases import City
from dao.daoConnection import Connection, DaoEmployee
from models.clases import Employees
from dao.daoConnection import Connection, DaoJobs
from models.clases import Jobs
os.system('cls')
#Conexion para base de datos laragon
conex = Connection("localhost", "root", "", "bdregisters")
conex.connect()


def insertarCiudad():
    nombre = input("Escribe el nombre de la Ciudad: ")
    ciudad = City(0, nombre, 1 )
    daoC = DaoCity(conex)
    daoC.insert(ciudad)

def mostrarCiudad():
    daoC = DaoCity(conex)
    registros = daoC.get_all()
    for ciudad in registros:
        print(ciudad)

def editarCiudad():
    daoC = DaoCity(conex)
    id= input("Inserta el id de la ciudad a modificar: ")
    nombre = input("Inserta nombre: ")
    ciudad = City(id, nombre)
    registU = daoC.update(ciudad)

def eliminarCiudad():
    daoC = DaoCity(conex)
    id = input("Inserta el id de la ciudad a eliminar: ")
    ciudad = City(id=id)
    registE = daoC.delete((ciudad.id,))

''' 
print("Agregar Registro")
insertarCiudad()
print("Mostrar Ciudad")
mostrarCiudad()

editarCiudad()

print("Mostrar Ciudad")
mostrarCiudad()

eliminarCiudad()

print("Mostrar Ciudad")
mostrarCiudad() 
'''

def insertarEmpleado():
    # Mostrar ciudades disponibles y solicitar al usuario que seleccione una
    mostrarCiudad()
    ciudad_id = input("Inserta el ID de la ciudad del empleado: ")
    # Ver puestos de trabajo y solicitar al usuario que seleccione uno
    mostrarTrabajos()

    nombre = input("Escribe el nombre del empleado: ")
    salario = input("Inserta el salario del empleado: ")
    status = input("Inserta el estado del empleado (1 para activo, 0 para inactivo): ")
    
    # Crear objeto Employee con los datos proporcionados
    empleado = Employees(id=0, name=nombre, ciudad_id=ciudad_id, salario=salario, status=status)
    
    # Crear instancia de DaoEmployee y llamar al método insert
    daoE = DaoEmployee(conex)
    daoE.insert(empleado)


def mostrarEmpleados():
    daoE = DaoEmployee(conex)
    registros = daoE.get_all()
    for empleado in registros:
        print(empleado)

def editarEmpleado():
    daoE = DaoEmployee(conex)
    id_empleado = input("Inserta el id del empleado a modificar: ")
    nombre = input("Inserta el nuevo nombre del empleado: ")
    ciudad_id = input("Inserta el nuevo ID de la ciudad del empleado: ")
    jobs_id = input("Inserta el nuevo ID del trabajo del empleado: ")
    salario = input("Inserta el nuevo salario del empleado: ")
    status = input("Inserta el nuevo estado del empleado (1 para activo, 0 para inactivo): ")
    
    # Crear objeto Employee con los datos actualizados
    empleado = Employees(id=id_empleado, name=nombre, ciudad_id=ciudad_id, jobs_id=jobs_id, salary=salario, status=status)
    
    # Llamar al método update del DaoEmployee
    daoE.update(empleado)

def eliminarEmpleado():
    daoE = DaoEmployee(conex)
    id_empleado = input("Inserta el id del empleado a eliminar: ")
    
    # Llamar al método delete del DaoEmployee
    daoE.delete(id_empleado)

#insertarEmpleado()
#print("Mostrar empleados")
#mostrarEmpleados()

def insertarTrabajo():
    nombre = input("Escribe el nombre del trabajo: ")
    estado = input("Inserta el estado del trabajo (1 para activo, 0 para inactivo): ")
    
    # Crear objeto Jobs con los datos proporcionados
    trabajo = Jobs(id=0, name=nombre, status=estado)
    
    # Crear instancia de DaoJobs y llamar al método insert
    daoJ = DaoJobs(conex)
    daoJ.insert(trabajo)

def mostrarTrabajos():
    daoJ = DaoJobs(conex)
    registros = daoJ.get_all()
    for trabajo in registros:
        print(trabajo)

def editarTrabajo():
    daoJ = DaoJobs(conex)
    id_trabajo = input("Inserta el id del trabajo a modificar: ")
    nombre = input("Inserta el nuevo nombre del trabajo: ")
    estado = input("Inserta el nuevo estado del trabajo (1 para activo, 0 para inactivo): ")
    
    # Crear objeto Jobs con los datos actualizados
    trabajo = Jobs(id=id_trabajo, name=nombre, status=estado)
    
    # Llamar al método update del DaoJobs
    daoJ.update(trabajo)

def eliminarTrabajo():
    daoJ = DaoJobs(conex)
    id_trabajo = input("Inserta el id del trabajo a eliminar: ")
    
    # Llamar al método delete del DaoJobs
    daoJ.delete(id_trabajo)

# Ejecutar las funciones
insertarTrabajo()
print("Mostrar trabajos")
mostrarTrabajos()
