"""
Insertar palabra nueva

Pedir por teclado: 
    - palabra alemana
    - traducción
    - nivel
    - tema
Insertar en SQLite
Extra: contral errores si faltan campos
"""

import sqlite3
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "vocabulario.db"
ruta = OUTPUT_DIR / name

# Pedir palabra

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

