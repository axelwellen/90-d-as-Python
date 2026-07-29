"""
    Crear base de datos de vocabulario
    Crear vocabulario.db con tabla: 
    - palabras(id, palabra_de, traduccion_es, nivel, tema)
    insertar 5 palabras
"""

import sqlite3
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "vocabulario.db"
ruta = OUTPUT_DIR / name

palabras = [
        ("verschieden", "distinto", "A1", "alltag"),
        ("gehorsam","obediente","B1","tier"),
        ("Himmel","cielo","A1","wetter"),
        ("fremd","extraño","A2","alltag"),
        ("nah","cerca","A2","alltag")
        ]

# creamos la BBDD y añadimos las palabras
with sqlite3.connect(ruta) as conexion:
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra_de TEXT NOT NULL UNIQUE,
            traduccion_es TEXT, 
            nivel TEXT,
            tema TEXT
            )
            """)

    # Añadimos palabras a la BBDD si no existen
    for palabra in palabras: 
        cursor.execute("""
                INSERT OR IGNORE INTO palabras (palabra_de, traduccion_es, nivel, tema) 
                VALUES (?,?,?,?)
            """, palabra) # los parámetros van juntos como una tupla

        if cursor.rowcount == 0: 
            print(f"{palabra[0]} ya existía")
        else: 
            print(f"{palabra[0]} añadida")

