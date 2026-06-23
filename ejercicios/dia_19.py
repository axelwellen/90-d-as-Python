# Calculadora de funciones


def sumar(a,b):
    return (a+b)

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "error, division by zero"
a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))
opcion = input("Introduce una opción: \n1) Sumar\n2) Restar\n3) Multiplicar\n4) Dividir\n--> ")
match opcion:
    case "1":
        print(a, "+", b, "=", sumar(a,b))
    case "2":
        print(a, "-", b, "=", restar(a,b))
    case "3":
        print(a, "*", b, "=", multiplicar(a,b))
    case "4": 
        print(a, "/", b, "=", dividir(a,b))
    case _:
        print("Opción no válida")
