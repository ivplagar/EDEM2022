class Persona: #Objeto para guardar los datos de los clientes
  def __init__(self, nif, nombre, apellidos, telefono, email, preferente):
    self.nif = nif
    self.nombre = nombre
    self.apellidos = apellidos
    self.telefono = telefono
    self.email = email
    self.preferente = preferente