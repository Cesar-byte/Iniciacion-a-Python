import time


hora=time.localtime().tm_hour
minuto=time.localtime().tm_min
if hora < 19:
    print("faltan:",18-hora, "horas y", 59-minuto,"minutos")
else:
    print("Ya se termino el trabao")