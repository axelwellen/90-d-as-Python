# Generador de novmbres de archivo
# uso: python dia_33.py reporte semanal txt
# salida: reporte_semanal.txt
# Extra: añadir_fecha_actual al nombre

import sys
import datetime

extension = sys.argv[-1]

nombre = "_".join(sys.argv[1:-1])
dt = datetime.datetime.now()
nombre += f"_{dt.year}{dt.month:02d}{dt.day:02d}"
nombre += "." + extension
print(nombre)
