# Mini checkpoint: gestor de tareas
#
# Crear un programa que permita
# - añadir tarea
# - eliminar tarea
# - marcar tarea como hecha
# - mostrar pendientes
# - mostrar completadas
# Extra mostrar tareas en orden alfabético
# pop(n) y append a la vez en la lista de completadas
# tareas por número 0-5...

import os

condicion = True
lista = []
completadas = []

def printar_lista(lista):
    for i,tarea in enumerate(lista):
        print(i,tarea)

while condicion:
    try:
        opcion = int(input("--- MENU ---\n1) Añadir tarea\n2) Eliminar tarea\n3) Marcar tarea como hecha\n4) Ver tareas pendientes\n5) Ver tareas completadas\n6) Salir\n-->"))
    except ValueError:
        os.system("clear")
        print("La opción introducida debe ser un número")
        continue
    if opcion == 1:
        elemento = input("Qué tarea quieres añadir a la lista: ")
        lista.append(elemento)
        lista.sort()
        os.system("clear")
        print("Se ha añadido a la lista:", elemento)
    elif opcion == 2:
        os.system("clear")
        if not lista:
            print("No hay tareas pendientes")
        else:
            printar_lista(lista)
            try:
                n = int(input("Qué tarea quieres eliminar? --> "))
            except ValueError:
                print("La opción introducida debe ser un número")
                continue
            if 0<= n < len(lista):
                elemento = lista.pop(n)
                print("Se ha eliminado la tarea:", elemento)
            else:
                print("El número no corresponde con ninguna tarea")
    elif opcion == 3:
        os.system("clear")
        if not lista:
            print("No hay tareas pendientes")
        else:
            printar_lista(lista)
            try: 
                n = int(input("Qué tarea marcas como completada? --> "))
            except ValueError:
                print("La opción introducida debe ser un número")
                continue
            if 0<= n < len(lista):
                elemento = lista.pop(n)
                completadas.append(elemento)
                completadas.sort()
                print("Se ha completado la tarea:", elemento)
            else:
                print("El número no corresponde con ninguna tarea")
    elif opcion == 4:
        os.system("clear")
        print("Tareas de la lista:")
        printar_lista(lista)
    elif opcion == 5:
        os.system("clear")
        print("Tareas completadas:")
        printar_lista(completadas)
    elif opcion == 6:
        os.system("clear")
        print("Hasta pronto!")
        condicion = False
    else:
        os.system("clear")
        print("Opción introducida no válida")

