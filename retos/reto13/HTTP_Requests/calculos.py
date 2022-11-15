import math

def calcular_area_triangulo():
    base = float(input("Introduce la base del triángulo (cm): "))
    altura = float(input("Introduce la altura del triángulo (cm): "))
    area = (base * altura)/2
    print(f"El área del triángulo con base {base} cm y altura {altura} cm es igual a {area} cm cuadrados")

def calcular_area_circulo():
    radius = float(input("Introduce el radio del circulo: "))
    area_circulo = math.pi * radius**2
    print(f"El área de un círculo con radio {radius} cm es igual a {area_circulo} cm cuadrados")