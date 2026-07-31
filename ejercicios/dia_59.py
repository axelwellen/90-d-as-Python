"""
    Filtrar por nivel
    Pedir un nivel (A1, B2, ...)
    Mostrar solo palabras de ese nivel
    Extra: Si no hay resultado mostrar mensaje amable 
"""

import sqlite3
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "vocabulario.db"
ruta = OUTPUT_DIR / name

nivel = input("Indica un nivel (ej: A1,A2,B1,...): ")

# accedemos a la BBDD y guardamos todo el contenido
with sqlite3.connect(ruta) as conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM palabras WHERE nivel = ?",(nivel,))
    vocabulario = cursor.fetchall()

if vocabulario:
    for palabra in vocabulario: 
        print(f"{palabra[1]} -> {palabra[2]} [{palabra[3]}/{palabra[4]}]")
else: 
    print(f"Lo lamentamos. No hay palabras del nivel {nivel}")
