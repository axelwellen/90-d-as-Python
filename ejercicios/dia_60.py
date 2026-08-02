"""
Filtrar por temas

Pedir un tema y mostrar palabras de ese tema.
Extra: permitir búsqueda parcial con LIKE
"""
import sqlite3
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "vocabulario.db"
ruta = OUTPUT_DIR / name

tema = input("Indica un tema (ej: alltag, arbeit, essen, ...): ").strip().lower()

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
