# Mini checkpoint: Herramienta interactiva segura
#
# Crear un programa con menú
# 1 validad contraseña, 2 Validar IP, 3 Classificar HTTP, 4 salir
from dia_02 import es_segura
from dia_04 import clasificar_codigo
from dia_25 import es_ip_valida

while True:
    try:
        opcion = int(input("Introduce una opción\n1) Validar contraseña\n2) Validar IP\n3) Clasificar HTTP\n4) Salir\n--> "))
    except ValueError:
        print("Debes introducir un número entre 1 y 4")
        continue
    if opcion == 4:
        print("Hasta pronto!")
        break
    elif opcion == 1:
        op = input("Introduce una contraseña para validar: ")
        es_segura(op)
    elif opcion == 2:
        op = input("Introduce una IP: ")
        if es_ip_valida(op):
            print("La IP es correcta")
        else: 
            print("La IP no es correcta")
    elif opcion == 3:
        try:
            op = int(input("Introduce un código HTTP para validar: "))
            print(clasificar_codigo(op))
        except ValueError:
            print("El valor introducido no es compatible")
    else: 
        print("Introduce un número entre 1 y 4")
