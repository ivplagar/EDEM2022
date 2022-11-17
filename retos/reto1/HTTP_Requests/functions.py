import HTTP_Requests.discos as discos
from datetime import date

class Compra:
  def __init__(self, discos, precio, descuento):
    self.discos = discos
    self.precio = precio
    self.descuento = descuento
    
compraDisco = Compra("", 0, 0)

hoy = date.today()
formato = hoy.strftime("%d/%m/%Y")

def tienda():
  discoUno = discos.uno()
  discoDos = discos.dos()
  discoTres = discos.tres()
  discoCuatro = discos.cuatro()
  discoCinco = discos.cinco()
  discoSeis = discos.seis()
  discoSiete =  discos.siete()
  comprar = 1

  while comprar != 0:
    print("Catalogo (los discos de Black Metal y Electro tienen un descuento del 30%):")
    print(f"1: {discoUno.get('nombre')} - {discoUno.get('artista')} - {discoUno.get('precio')} € - {discoUno.get('año')} - {discoUno.get('genero')}")
    print(f"2: {discoDos.get('nombre')} - {discoDos.get('artista')} - {discoDos.get('precio')} € - {discoDos.get('año')} - {discoDos.get('genero')}")
    print(f"3: {discoTres.get('nombre')} - {discoTres.get('artista')} - {discoTres.get('precio')} € - {discoTres.get('año')} - {discoTres.get('genero')}")
    print(f"4: {discoCuatro.get('nombre')} - {discoCuatro.get('artista')} - {discoCuatro.get('precio')} € - {discoCuatro.get('año')} - {discoCuatro.get('genero')}")
    print(f"5: {discoCinco.get('nombre')} - {discoCinco.get('artista')} - {discoCinco.get('precio')} € - {discoCinco.get('año')} - {discoCinco.get('genero')}")
    print(f"6: {discoSeis.get('nombre')} - {discoSeis.get('artista')} - {discoSeis.get('precio')} € - {discoSeis.get('año')} - {discoSeis.get('genero')}")
    print(f"7: {discoSiete.get('nombre')} - {discoSiete.get('artista')} - {discoSiete.get('precio')} € - {discoSiete.get('año')} - {discoSiete.get('genero')}")
    comprar = int(input("Introduce el número del disco que quieres comprar. Para finalizar tu compra, pulsa 0: "))
    if(comprar == 1):
      compraDisco.discos = compraDisco.discos + discoUno.get('nombre') + ", "
      compraDisco.precio = compraDisco.precio + discoUno.get('precio')
      compraDisco.descuento = compraDisco.descuento + 0
      print("Has comprado el disco 1")
    elif(comprar == 2):
      compraDisco.discos = compraDisco.discos + discoDos.get('nombre') + ", "
      compraDisco.precio = compraDisco.precio + (discoDos.get('precio') - discoDos.get('precio') * 0.3)
      compraDisco.descuento = compraDisco.descuento + (discoDos.get('precio') * 0.3)
      print("Has comprado el disco 2")
    elif(comprar == 3):
      compraDisco.discos = compraDisco.discos + discoTres.get('nombre') + ", "
      compraDisco.precio = compraDisco.precio + discoTres.get('precio')
      compraDisco.descuento = compraDisco.descuento + 0
      print("Has comprado el disco 3")
    elif(comprar == 4):
      compraDisco.discos = compraDisco.discos + discoCuatro.get('nombre') + ", "
      compraDisco.precio = compraDisco.precio + discoCuatro.get('precio')
      compraDisco.descuento = compraDisco.descuento + 0
      print("Has comprado el disco 4")
    elif(comprar == 5):
      compraDisco.discos = compraDisco.discos + discoCinco.get('nombre') + ", "
      compraDisco.precio = compraDisco.precio + discoCinco.get('precio')
      compraDisco.descuento = compraDisco.descuento + 0
      print("Has comprado el disco 5")
    elif(comprar == 6):
      compraDisco.discos = compraDisco.discos + discoSeis.get('nombre') + ", "
      compraDisco.precio = compraDisco.precio + discoSeis.get('precio')
      compraDisco.descuento = compraDisco.descuento + 0
      print("Has comprado el disco 6")
    elif(comprar == 7):
      compraDisco.discos = compraDisco.discos + discoSiete.get('nombre') + ", "
      compraDisco.precio = compraDisco.precio + (discoSiete.get('precio') - discoSiete.get('precio') * 0.3)
      compraDisco.descuento = compraDisco.descuento + (discoSiete.get('precio') * 0.3)
      print("Has comprado el disco 7")
  else:
    print(f"Has comprado los discos: {compraDisco.discos}\nTotal gastado: {round(compraDisco.precio, 2)}\nDescuento total: {round(compraDisco.descuento, 2)}\nFecha de compra: {formato}")