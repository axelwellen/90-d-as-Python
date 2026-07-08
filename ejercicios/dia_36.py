# Contador de líneas
# 
# Crear un script que lea datos.txt y muestre cuantas líneas tiene
# Extra: recibe el nombre del archivo por terminal
# Extra: indicar el directorio donde se encuentra el archivo
import sys
from pathlib import Path

if len(sys.argv) > 1:
    nombre = sys.argv[1]
    if len(sys.argv) > 2:
        ruta = Path(sys.argv[2]) / nombre
    else:
        OUTPUTS_DIR = Path(__file__).resolve().parent.parent / "outputs"
        ruta = OUTPUTS_DIR / nombre
else:
    print("El formato debe ser:\npython dia_36.py [nombre_archivo] [(Opcional) directorio]")
    exit()
# tenemos que leer el archivo y ver cuantas lineas tiene
with open(ruta, "r", encoding = "utf-8") as fichero:
    lineas = len(fichero.readlines())

print("El archivo",nombre,"tiene",lineas,"líneas")
