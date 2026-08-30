"""
Este es el main desde donde llamaraemos a las diferentes funciones de database.py
"""
from database import *
from utils import leer_entero
import os



os.system("clear")
while True: 
    opcion = leer_entero("Bienvenido a la mini BBDD de alemán\n\nSelecciona una opción:\n1) Buscar palabras\n2) Filtrar por nivel\n3) Añadir palabra\n4) Salir\n--> ")
    if opcion == 1:
        os.system("clear")
        print("Opción seleccionada -> Buscar palabras")
        busqueda = input("Dime que palabra quieres buscar: ")
        palabras = obtener_palabra(busqueda)
        if palabras is not None:
            for palabra in palabras: 
                print(f"{palabra[1]} -> {palabra[2]} [{palabra[3]}/{palabra[4]}]")
    elif opcion == 2: 
        os.system("clear")
        print("Opción seleccionada -> Filtrar por nivel")
        nivel = input("Por qué nivel quieres filtrar: ")
        if nivel in ["A1","A2","B1","B2","C1","C2"]:
            palabras = filtrar_por_nivel(nivel)
        else: 
            print("Nivel no válido")
        if palabras is not None:
            for palabra in palabras: 
                print(f"{palabra[1]} -> {palabra[2]} [{palabra[3]}/{palabra[4]}]")

    elif opcion == 3: 
        os.system("clear")
        print("Opción seleccionada -> Añadir palabra")
        while True: 
            palabra_de = input("Introduce una nueva palabra: ").strip()
            traduccion_es = input("Introduce la traducción de la palabra: ").strip()
            nivel = input("Introduce el nivel de la palabra: ").strip().upper()
            tema = input("Introduce el tema de la palabra: ").strip()
            if palabra_de and traduccion_es and nivel and tema:
                verif = input(f"Se van a introducir los siguientes datos:\n - palabra: {palabra_de}\n - traducción: {traduccion_es}\n - nivel: {nivel}\n - tema: {tema}\nSon correctos todos los datos [y/n]? ")
                if verif.lower() == "y":
                    break
            print("Datos incorrectos, volver a introducir los datos!")
        print(insertar_palabra(palabra_de, traduccion_es, nivel, tema))
    
    elif opcion == 4:
        print("Hasta pronto")
        exit()

    else:
        os.system("clear")
        print("Introduce una opción válida")

