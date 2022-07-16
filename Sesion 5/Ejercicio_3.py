def bisiesto (year=0):
    if year % 4 == 0 and year % 100 == 0 and year % 400 ==0 :
        return "El año "+str(year)+" es un año bisiesto"
    else:
        return "El año "+str(year)+" no es un año bisiesto"

print(bisiesto(2400))