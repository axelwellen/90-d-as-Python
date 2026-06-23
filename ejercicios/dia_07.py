# Mini checkpoint: herramientas de texto

# Crear un menú:
# 1. Limpiar texto
# 2. Contar palabras
# 3. Buscar palabras
# 4. Salir

import os
from dia_01 import limpiador_nombres_archivo
from dia_03 import contar_palabras
from dia_05 import buscador_palabra_frase
condicion = True
os.system("clear")

while condicion:
    try:
        opcion = int(input("Bienvenido al menú\n\t1. Limpiar texto\n\t2. Contar palabras\n\t3. Buscar palabras\n\t4. Salir\nOpción: "))
    except ValueError:
        os.system("clear")
        print("La opción introducida debe ser un número!")
        continue
    if opcion == 1:
        os.system("clear")
        print("Opción seleccionada -> Limpiar texto")
        # limpiador de nombres de archivo (día 01)
        lista_archivos = input("Introduce una lista de nombres de archivos separados por ',': ")
        lista_archivos_ordenados = limpiador_nombres_archivo(lista_archivos.split(","))
        for a in lista_archivos_ordenados:
            print("-> ", a)
    
    elif opcion == 2:
        os.system("clear")
        print("Opción seleccionada -> Contar palabras")
        # contador de palabras (día 03)
        text = input("Introduce las palabras que quieras contas separadas por un espacio: ")
        diccionario_palabras = contar_palabras(text)
        for clave, valor in diccionario_palabras.items():
            print(clave, "-->", valor)

    elif opcion == 3:
        os.system("clear")
        print("Opción seleccionada -> Buscar palabras")
        # buscador de palabras (día 05)
        frase = input("Introduce una frase: ")
        palabra = input("Introduce una palabra a buscar en la frase: ")
        buscador_palabra_frase(frase,palabra)
    elif opcion == 4:
        condicion = False
        print("Hasta pronto!")
    else:
        os.system("clear")
        print("Introduce de nuevo una opción válida")



