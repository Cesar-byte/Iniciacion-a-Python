inicio = int(input("Introduzca el numero de inicio: "))
final = int (input("Introduzca el numero final: "))

for i in range(inicio,final):
    if i%2 != 0:
        print(i)