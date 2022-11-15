import math

def calcular_volumen_cilindro():    
    area = calcular_area_circulo()
    longitud = float(input("Introduce la longitud del cilindro (cm): "))
    volumen = area * longitud
    print(f"El volumen del cilindro con longitudo {longitud} cm es igual a {volumen} cm cúbicos")

def calcular_area_circulo():
    radius = float(input("Introduce el radio del circulo: "))
    area_circulo = math.pi * radius**2
    return area_circulo