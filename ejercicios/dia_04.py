# Clasificador de códigos HTTP
# pedimos un código HTTP y devolvemos la salida en función del código

codigo = input("Introduce un código HTTP: ")

def clasificar_codigo(codigo):
    match codigo:
        case cod if 200 <= cod <= 299:
            return "Éxito"
        case cod if 300 <= cod <= 399:
            return "Redirección"
        case cod if 400 <= cod <= 499:
            return "Error Cliente"
        case cod if 500 <= cod <= 599:
            return "Error Servidor"
        case _:
            return "Código no válido"

try:
    codigo = int(codigo)
    print(clasificar_codigo(codigo))
except ValueError:
    print("El código introducido no es un número")


