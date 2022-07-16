def esPrimo(x):
    for i in range(2,x-1):
        if x % i == 0:
            break
    else:
        return "El numero "+ str(x)+ " es primo"
    
    return "El numero "+ str(x)+ " no es primo"


print(esPrimo(31))