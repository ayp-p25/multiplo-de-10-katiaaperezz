"""
Múltiplo de 10
"""
try:
# Entradas
    numero=int(input("Introduzca un número: "))

# Proceso
    if numero % 10 == 0:
        print("El número",numero, "sí es múltiplo de 10")
    else: 
        print("El número",numero, "no es múltiplo de 10")
except ValueError:
    print("Error, intenta de nuevo.")        