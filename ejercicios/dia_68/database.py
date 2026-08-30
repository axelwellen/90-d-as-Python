"""
Aquí cogeremos el vocabulario de SQLite y organizaremos algunas funciones como:
    - conectar_db
    - obtener_palabra
    - insertar_palabra
    - filtrar_por_nivel
Extra: separamos en dos archivos database.py y main.py
"""
import sqlite3
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent.parent / "outputs"
name = "vocabulario.db"
ruta = OUTPUT_DIR / name

# conectamos con la base de datos
def conectar_db():
    conexion = sqlite3.connect(ruta)
    cursor = conexion.cursor()
    return cursor

# obtener palabra de la BBDD
def obtener_palabra(palabra):
    cursor = conectar_db()
    cursor.execute("SELECT * FROM palabras WHERE palabra_de LIKE ? OR traduccion_es LIKE ?",(f"%{palabra}%", f"%{palabra}%"))
    vocabulario = cursor.fetchall()

    if vocabulario:
        return vocabulario
    else:
        return None

def insertar_palabra(palabra_de, traduccion_es, nivel, tema):
    palabra = (palabra_de, traduccion_es, nivel, tema)
    with sqlite3.connect(ruta) as conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT OR IGNORE INTO palabras (palabra_de, traduccion_es, nivel, tema) VALUES (?,?,?,?)", palabra)
        if cursor.rowcount == 0: 
            return "La palabra ya existía"
        else: 
            return f"Palabra {palabra_de} añadida"

def filtrar_por_nivel(nivel):
    with sqlite3.connect(ruta) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM palabras WHERE nivel = ?",(nivel,))
        vocabulario = cursor.fetchall()
        if vocabulario: 
            return vocabulario
        else: 
            return None

