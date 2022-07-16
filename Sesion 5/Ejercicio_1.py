from math import pi
from xml.etree.ElementTree import PI


def areaTiangulo (altura=0, base=0):
    return altura*base/2

areaCirculo = lambda radio: pi*(radio**2)

print("El area de un triangulo de base 2 y altura 14 es:", areaTiangulo(14,2))
print("El area de un circulo de radio 12 es :", areaCirculo(12))
