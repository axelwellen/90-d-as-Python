"""
    Mini checkpoint: vocabulario terminal v1

    Crear una mini app por termina que permita: 
    1 Ver palabras
    2 Filtrar por nivel
    3 Filtrar por tema
    4 Añadir palabra
    5 Pregunta aleatoria
    6 Salir
"""
import os
import sqlite3
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "vocabulario.db"
ruta = OUTPUT_DIR / name

# accedemos a la BBDD y mostramos todas las palabras
def mostrar_palabras():
    with sqlite3.connect(ruta) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM palabras ORDER BY nivel")
        vocabulario = cursor.fetchall()

    for palabra in vocabulario:
        print(f"{palabra[1]} -> {palabra[2]} [{palabra[3]}/{palabra[4]}]")

# accedemos a la BBDD y mostrarmos todas las palabras por nivel
def filtrar_por_nivel(nivel):
    with sqlite3.connect(ruta) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM palabras WHERE nivel = ?",(nivel,))
        vocabulario = cursor.fetchall()

    if vocabulario:
        for palabra in vocabulario:
            print(f"{palabra[1]} -> {palabra[2]} [{palabra[3]}/{palabra[4]}]")
    else:
        print(f"Lo lamentamos. No hay palabras del nivel {nivel}")

# accedemos a la BBDD y mostramos las palabras por tema
def filtrar_por_tema(tema):
	# accedemos a la BBDD y guardamos todo el contenido
	with sqlite3.connect(ruta) as conexion:
	    cursor = conexion.cursor()
	    cursor.execute("SELECT * FROM palabras WHERE tema LIKE ?",(f"%{tema}%",))
	    vocabulario = cursor.fetchall()
	
	if vocabulario:
	    for palabra in vocabulario:
	        print(f"{palabra[1]} -> {palabra[2]} [{palabra[3]}/{palabra[4]}]")
	else:
	    print(f"Lo lamentamos. No hay palabras que contengan el tema {tema}")

# añadimos palabra a la BBDD
def add_palabra():
	while True:
	    palabra_de = input("Introduce una nueva palabra: ").strip()
	    traduccion_es = input("Introduce la traducción de la palabra: ").strip()
	    nivel = input("Introduce el nivel de la palabra: ").strip()
	    tema = input("Introduce el tema de la palabra: ").strip()
	    if palabra_de and traduccion_es and nivel and tema:
	        verif = input(f"Se van a introducir los siguientes datos:\n - palabra: {palabra_de}\n - traducción: {traduccion_es}\n - nivel: {nivel}\n - tema: {tema}\nSon correctos todos los datos [y/n]? ")
	        if verif.lower() == "y":
	            break
	    print("Datos incorrectos, volver a introducir los datos!")
	
	palabra = (palabra_de, traduccion_es, nivel, tema)
	
	# accedemos a la BBDD y guardamos todo el contenido
	with sqlite3.connect(ruta) as conexion:
	    cursor = conexion.cursor()
	    cursor.execute("INSERT OR IGNORE INTO palabras (palabra_de, traduccion_es, nivel, tema) VALUES (?,?,?,?)",palabra)
	    if cursor.rowcount == 0:
	        print("La palabra ya existía")
	    else:
	        print(f"Palabra {palabra_de} añadida")

def preguntar_palabra_aleatoria():
# Seleccionar palabra aleatoria y mostrarla
    with sqlite3.connect(ruta) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM palabras ORDER BY RANDOM() LIMIT 1") # LIMIT 1 nos selecciona solo 1
        palabra = cursor.fetchone()

    trad = input(f"Cuál es la traducción de {palabra[1]}? ")
    if trad.strip().lower() == palabra[2].lower():
        print(f"Correcto, la traducción de {palabra[1]} es {palabra[2]}")
    else:
        print(f"Incorrecto, la traducción de {palabra[1]} es {palabra[2]}")

os.system("clear")
while True:
    try: 
        opcion = int(input("Bienvenido a la mini BBDD de alemán\n\nSelecciona una opción:\n1) Ver palabras\n2) Filtrar por nivel\n3) Filtrar por tema\n4) Añadir palabra\n5) Pregunta aleatoria\n6) Salir\n--> "))
    except ValueError:
        os.system("clear")
        print("La opción introducida debe ser un número entre 1 y 6")
        continue
    if opcion == 1: 
        os.system("clear")
        print("Opción seleccionada: Ver todas las palabras\n")
        mostrar_palabras()
    elif opcion == 2: 
        os.system("clear")
        nivel = input("Indica un nivel (ej: A1, A2, B1, ...): ")
        filtrar_por_nivel(nivel)
    elif opcion == 3: 
        os.system("clear")
        tema = input("Introduce un tema (ej: alltag, arbeit, esse, ...): ")
        filtrar_por_tema(tema)
    elif opcion == 4: 
        os.system("clear")
        add_palabra()
    elif opcion == 5: 
        os.system("clear")
        preguntar_palabra_aleatoria()
    elif opcion == 6:
        print("Hasta pronto!")
        exit()
    else: 
        os.system("clear")
        print("Introduce de nuevo una opción válida")
