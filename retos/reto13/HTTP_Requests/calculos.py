import math

def calcular_area_triangulo():
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    area = (base * altura)/2
    print(f"El área del triángul con base {base} y la altura {altura} es igual a {area}")

def calcular_area_circulo():
    radius = float(input("Introduce el radio del circulo: "))
    area_circulo = math.pi * radius**2
    print(f"El área de un círculo con radio {radius} es igual a {area_circulo}")