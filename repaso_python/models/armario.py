from producto import Producto
class Armario(Producto):
    puertas: int
    altura: float
    ancho: float
    def __init__(self, nombre, precio, categoria, coste, color, puertas, altura, ancho):
        super().__init__(nombre, precio, categoria, coste, color)
        self.puertas = puertas
        self.altura = altura
        self.ancho = ancho