import HTTP_Requests.discos as discos

'''def catalogo():
  discos_catalogo = discos
  for disco in discos_catalogo:
    input'''


def tienda():
  discoUno = discos.uno()
  discoDos = discos.dos()
  discoTres = discos.tres()
  discoCuatro = discos.cuatro()
  discoCinco = discos.cinco()
  discoSeis = discos.seis()
  discoSiete =  discos.siete()
  print(f"Catálogo: \n 1.-{discoUno.get('nombre')} \n 2.-{discoDos.get('nombre')} \n 3.-{discoTres.get('nombre')} \n 4.-{discoCuatro.get('nombre')} \n 5.-{discoCinco.get('nombre')} \n 6.-{discoSeis.get('nombre')} \n 7.-{discoSiete.get('nombre')}:\n")
  #discoComprado = input(f"Elige el disco que quieres comprar: \n 1.-{discoUno.get('nombre')} - {discoUno.get('artista')} : {discoUno.get('precio')}\n 2.-{discoDos.get('nombre')} \n 3.-{discoTres.get('nombre')} \n 4.-{discoCuatro.get('nombre')} \n 5.-{discoCinco.get('nombre')} \n 6.-{discoSeis.get('nombre')} \n 7.-{discoSiete.get('nombre')}:\n")
  comprar = 1
  while comprar != 0:
    comprar = int(input("Introduce el número del disco que quieres comprar. Para finalizar tu compra, pulsa 0"))
    print("hola")
    '''if(comprar == 1):
      print("Has comprado el disco 1")
    else:
      print("No has comprado el disco 1")'''
  else:
    print("Has comprado")