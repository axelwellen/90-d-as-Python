# Calculadora robusta
#
# repetir la calculadora del día 19
# contrlar entradas inválidas
# controlar división por 0
# no rompe el programa
# Extra: Bucle para hacer varias operaciones

from dia_19 import sumar, restar, multiplicar, dividir


if __name__ == "__main__":
    condicion = True
    while condicion:
        operacion = input("Introduce una operacion: ")
        op = operacion.split()
        try:
            a = int(op[0])
            b = int(op[2])
        except ValueError, IndexError:
            print("Debes introducir el formato: numero operador numero (ej: 45 + 78)")
            continue
        try:
            if op[3] == "=":
                condicion = False
                string = ""
        except IndexError:
            string = "\nPuedes introducir más operaciones hasta escribir '=' (ej: 15 + 48 =)"
        match op[1]:
            case "+":
                print(a, "+", b, "=", sumar(a,b), string)
            case "-":
                print(a, "-", b, "=", restar(a,b), string)
            case "*":
                print(a, "*", b, "=", multiplicar(a,b), string)
            case "/":
                print(a, "/", b, "=", dividir(a,b), string)
            case _:
                print("Opción no válida, introduce una operación con el formato: numero operador numero")

