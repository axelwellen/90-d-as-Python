"""
Palabra aleatoria

Sacar una palabra aleatoria de la BBDD
Mostrar la palabra alemana, pedir traducción y luego mostrar la correcta
Extra: contar acierto/error
"""
import sqlite3
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "vocabulario.db"
ruta = OUTPUT_DIR / name

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
