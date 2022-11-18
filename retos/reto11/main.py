from HTTP_Requests.functions import anyadir as new

while True:
    new()
    plantilla = new()
    for empleado in plantilla:
        print(empleado.nif,empleado.nombre,empleado.apellidos,empleado.telefono,empleado.email)