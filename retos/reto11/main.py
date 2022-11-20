from HTTP_Requests.functions import anyadir as new
from HTTP_Requests.functions import eliminar as delete
from HTTP_Requests.functions import mostrarNIF as showNIF
from HTTP_Requests.functions import mostrarTodos as showAll
from HTTP_Requests.functions import mostrarPreferentes as showPref
import sys
clientes = [] #Inicializamos la lista de clientes que usaremos durante todo el programa

while True:
    #Menú principal
    programa = input("**Clientes**\n1.Añadir un cliente\n2.Eliminar cliente por NIF\n3.Mostrar Cliente por NIF\n4.Listar TODOS los clientes\n5.Mostrar ÚNICAMENTE los clientes preferentes\n6.Finalizar Programa\n")
    if programa == "1":
        new(clientes) #Función para añadir clientes
    elif programa == "2":
        delete(clientes) #Función para eliminar clientes
    elif programa == "3":
        showNIF(clientes) #Función para mostrar clientes por NIF
    elif programa == "4":
        showAll(clientes) #Función para mostrar todos los clientes
    elif programa == "5":
        showPref(clientes) #Función para mostrar todos los clientes preferentes
    elif programa == "6":
        sys.exit() #Comando para salir
    else:
        print("Introduce una de las opciones de la lista")