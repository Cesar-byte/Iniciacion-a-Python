class Alumno:
    _nombre = None
    _nota = None

    def __init__(self, nombre, nota) -> None:
        self._nombre = nombre
        self._nota = nota

    def mostrar(self):
        if self._nota < 5:
            print (self._nombre, "ha suspendido el examen")
        else:
            print(self._nombre, "ha aprobado el examen")

persona1 = Alumno("Paco", 4.5)
persona1.mostrar()

persona2 = Alumno("Sofia", 8)
persona2.mostrar()