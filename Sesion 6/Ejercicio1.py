from asyncio import run_coroutine_threadsafe
from turtle import color


class Vehiculo:
    _color = None
    _ruedas = None
    _puertas = None

    def __init__(self, color, ruedas, puertas):
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas

class Coche(Vehiculo):
    _velocidad = None
    _cilindrada = None

    def __init__(self, color, ruedas, puertas,vel,cilind):
        super().__init__(color, ruedas, puertas)
        self._velocidad = vel
        self._cilindrada = cilind

    def mostrar(self):
        print("El coche de",self._ruedas,"ruedas,",self._color,"y",self._puertas,"puertas tiene una cilindrada de",self._cilindrada,"cm3 que le permite una velocidad de",self._velocidad,"km/h")


coche = Coche("Rojo", 4, 5, 130, 50)

coche.mostrar()

