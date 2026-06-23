# Simulador de pila (LIFO)
# Crear una pila de tareas: 
# Menu
# 1) Añadir tarea
# 2) Completar última tarea
# 3) Ver tareas
# 4) Salir
# Extra: Que no se pueda hacer pop si la pila está vacía

import os

condicion = True
lista = []

while condicion:
    try:
        opcion = int(input("--- MENU ---\n1) Añadir tarea\n2) Completar última tarea\n3) Ver tareas\n4) Salir\n-->"))
    except ValueError:
        os.system("clear")
        print("La opción introducida debe ser un número")
        continue
    if opcion == 1:
        elemento = input("Qué tarea quieres añadir a la lista: ")
        lista.append(elemento)
        os.system("clear")
        print("Se ha añadido a la lista:", elemento)
    elif opcion == 2:
        os.system("clear")
        if not lista:
            print("No hay tareas pendientes")
        else:
            elemento = lista.pop()
            print("Se ha completado la tarea:", elemento)
    elif opcion == 3:
        os.system("clear")
        print("Tareas de la lista:")
        for tarea in lista:
            print("-",tarea)
    elif opcion == 4:
        os.system("clear")
        print("Hasta pronto!")
        condicion = False
    else:
        os.system("clear")
        print("Opción introducida no válida")


