from HTTP_Requests.persona import Persona

def anyadir(clientes):
    persona = Persona("","","","","",True) #Objeto para guardar los datos introducidos en los inputs
    #Inputs para la introducción de datos
    nif = input("Introduce el NIF del cliente: ")
    nombre = input("Introduce el nombre del cliente: ")
    apellidos = input("Introduce los apellidos del cliente: ")
    telefono = input("Introduce el teléfono del cliente: ")
    email = input("Introduce el email del cliente: ")
    preferente = input("Escribe 1 si el usuario es preferente, 2 si no lo es: ")
    while True: #Bucle para obligar al usuario a introducir 1 o 2
        if preferente != "1" and preferente != "2":
            print("No has introducido 1 o 2.")
            preferente = input("Escribe 1 si el usuario es preferente, 2 si no lo es: ")
            continue
        elif preferente == "1":
            preferente = True
            break
        else:
            preferente = False
            break        
    persona = Persona(nif,nombre,apellidos,telefono,email,preferente) #Guardamos los datos del cliente
    clientes.append(persona) #Añadimos el cliente a la lista
    print(f"Has introducido el cliente con NIF: {persona.nif}") #Imprimios el NIF del cliente acabado de introducir
    return(clientes)

def eliminar(clientes):
    if clientes == []: #Aviso de que no hay clientes aún en la lista
        return print('No tienes clientes') 
    print("Estos son los NIF de los clientes que tienes: ")
    for cliente in clientes:
        print(f"{cliente.nif}") #Mostramos los NIF de los clientes que hay para que se elija cual eliminar
    nifEliminado = input("Introduce el NIF del cliente que quieres eliminar: ") 
    for cliente in clientes:
        if nifEliminado == cliente.nif: 
            print(f"Has eliminado el cliente con nif {cliente.nif}")
            clientes.remove(cliente) #Eliminamos el cliente
            print("Estos son los NIF de los clientes que tienes: ")
            for cliente in clientes:
                print(f"{cliente.nif}") #Mostramos los NIF de los clientes que quedan

def mostrarNIF(clientes):
    if clientes == []:
        return print('No tienes clientes') 
    print("Estos son los NIF de los clientes que tienes: ")
    for cliente in clientes:
        print(f"{cliente.nif}") #Mostramos los NIF de los clientes que hay
    nifMostrado = input("Introduce el NIF del cliente que quieres mostrar: ")
    for cliente in clientes:
        if nifMostrado == cliente.nif: #Comprobamos si existe en la lista algun cliente con el nif introducido
            print(f"NIF: {cliente.nif}\nNombre: {cliente.nombre}\nApellidos: {cliente.apellidos}\nTelefono: {cliente.telefono}\nEmail: {cliente.email}\nPreferente: {cliente.preferente}")

def mostrarTodos(clientes):
    if clientes == []:
        return print('No tienes clientes') 
    for cliente in clientes:
        #Mostramos todos los clientes
        print(f"NIF: {cliente.nif}\nNombre: {cliente.nombre}\nApellidos: {cliente.apellidos}\nTelefono: {cliente.telefono}\nEmail: {cliente.email}\nPreferente: {cliente.preferente}\n")

def mostrarPreferentes(clientes):
    if clientes == []:
        return print('No tienes clientes') 
    for cliente in clientes:
        if cliente.preferente == True: #Mostramos los clientes preferentes comprobando si los que hay son o no son preferentes
            print(f"NIF: {cliente.nif}\nNombre: {cliente.nombre}\nApellidos: {cliente.apellidos}\nTelefono: {cliente.telefono}\nEmail: {cliente.email}\nPreferente: Sí\n")

