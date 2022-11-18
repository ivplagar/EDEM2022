from HTTP_Requests.persona import Persona

def anyadir():
    persona = Persona("","","","","",True)
    nif = input("Introduce el NIF del empleado: ")
    nombre = input("Introduce el nombre del empleado: ")
    apellidos = input("Introduce los apellidos del empleado: ")
    telefono = input("Introduce el teléfono del empleado: ")
    email = input("Introduce el email del empleado: ")
    '''preferente = input("Escribe 1 si el usuario es preferente, 2 si no lo es: ")
    if (preferente == 1):
        pref = True
        #persona = Persona(nif,nombre,apellidos,telefono,email,pref)
    elif(preferente == 2):
        pref = False'''
        
    persona = Persona(nif,nombre,apellidos,telefono,email,True)
    plantilla = []
    plantilla.append(persona)
    return(plantilla)