import os
from dao.daoConnection import Connection, DaoCity
from models.clases import City

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

#def eliminarCiudad():
    #daoC = DaoCity(conex)
    #id= input("Inserta el id de la ciudad a eliminar: ")
    #ciudad = City(id)
    #registE = daoC.delete(ciudad)
    
def eliminarCiudad():
    daoC = DaoCity(conex)
    id = input("Inserta el id de la ciudad a eliminar: ")
    ciudad = City(id=id)
    registE = daoC.delete((ciudad.id,))
#print("Agregar Registro")
#insertarCiudad()


#print("Mostrar Ciudad")
#mostrarCiudad()

#editarCiudad()

print("Mostrar Ciudad")
mostrarCiudad()

eliminarCiudad()

print("Mostrar Ciudad")
mostrarCiudad()


