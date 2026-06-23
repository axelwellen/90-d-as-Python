# Simulador de cola (FIFO)
# Crear una cola de atención al cliente:
# Menu
# 1) Añadir cliente
# 2) Atender siguiente
# 3) Ver cola
# 4) Salir
# Extra: Mostrar cuantos clientes quedan

import os

condicion = True
cola = []

while condicion:
    try:
        opcion = int(input("--- MENU ---\n1) Añadir cliente\n2) Atender siguiente\n3) Ver cola\n4) Salir\n-->"))
    except ValueError:
        os.system("clear")
        print("La opción introducida debe ser un número")
        continue
    if opcion == 1:
        elemento = input("Qué cliente quieres añadir a la cola: ")
        cola.append(elemento)
        os.system("clear")
        print("Se ha añadido a la lista:", elemento)
    elif opcion == 2:
        os.system("clear")
        if not cola:
            print("No hay clientes pendientes")
        else:
            elemento = cola.pop(0)
            print("Se ha atendido a:", elemento)
    elif opcion == 3:
        os.system("clear")
        print("Cola pendiente:")
        for cliente in cola:
            print("-",cliente)
    elif opcion == 4:
        os.system("clear")
        print("Hasta pronto!")
        condicion = False
    else:
        os.system("clear")
        print("Opción introducida no válida")
