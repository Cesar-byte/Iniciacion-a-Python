import math

peso = float(input('Introduzca su peso (kg): '))

altura = float(input('Introduzca su altura (m): '))

imc=peso // (altura**2)

imc = round(imc,3)

print(imc)