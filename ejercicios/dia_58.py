""" 
    Consultar todas las palabras
    
    Leer la base de datos y mostrar todas las palabras
    Formato 
        Voraussetzung -> requisito [B2/trabajo]
    Extra: ordernar por nivel
"""
import sqlite3
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "vocabulario.db"
ruta = OUTPUT_DIR / name

# accedemos a la BBDD y guardamos todo el contenido
with sqlite3.connect(ruta) as conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM palabras ORDER BY nivel")
    vocabulario = cursor.fetchall()

for palabra in vocabulario: 
    print(f"{palabra[1]} -> {palabra[2]} [{palabra[3]}/{palabra[4]}]")
