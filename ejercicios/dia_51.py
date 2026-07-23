# Registro con timestamp
#
# Crear un script que añada una linea a registro.txt con fecha y hora actual
# 2026-06-03 11:30 - Estudié Python 20 min"
# Extra: Permitir pasar el mensaje por terminal

import sys
from pathlib import Path
import datetime

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "registro.txt"
ruta = OUTPUT_DIR / nombre

if len(sys.argv) == 2:
    frase = sys.argv[1]
    dt = datetime.datetime.now()
    with open(ruta, "a", encoding = "utf-8") as fichero: 
        fichero.write(f"{dt.year}-{dt.month:02d}-{dt.day:02d} {dt.hour:02d}:{dt.minute:02d} - {frase}\n")

else:
    print("El formato debe ser\n\t python dia_51.py 'frase que queramos registrar'")
