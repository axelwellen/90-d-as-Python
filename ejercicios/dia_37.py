# Buscador de archivo
# 
# Leer un archivo y buscar líneas que contengan una palabra
# ejemplo: python dia_37.py error logs.txt
# Extra: mostrar el número de línea

import sys
from pathlib import Path

if len(sys.argv) > 2:
    palabra = sys.argv[1]
    nombre = sys.argv[2]
    if len(sys.argv) > 3:
        ruta = Path(sys.argv[3]) / nombre
    else:
        OUTPUTS_DIR = Path(__file__).resolve().parent.parent / "outputs"
        ruta = OUTPUTS_DIR / nombre
else: 
    print("El formato debe ser:\npython dia_37.py [palabra_a_buscar] [nombre_archivo] [(opcional)directorio]")
    exit()

# Si todo está correcto, leemos el archivo y buscamos la palabra en las diferentes líneas. 
with open(ruta, "r", encoding = "utf-8") as fichero:
    lineas = fichero.readlines()

for i, linea in enumerate(lineas, start = 1):
    veces = linea.lower().count(palabra.lower()) # palabra
    if veces > 0:
        print(f"\033[34m{palabra}\033[0m aparece {veces} veces en la línea {i}")
        print("    ",linea.replace(palabra,f"\033[32m{palabra}\033[0m").strip())

