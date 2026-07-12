# Numerador de lineas
# 
# Leer un archivo y crear otro con líneas numeradas
# ejemplo: 
#     0001: primera línea
#     0002: segunda línea
# Extra: usa formato :04d

from pathlib import Path

OUTPUTS_DIR = Path(__file__).resolve().parent.parent / "outputs"
ruta_salida = OUTPUTS_DIR / "salida_numerada.txt"
ruta_entrada = OUTPUTS_DIR / "documento_a_numerar.txt"

with open(ruta_entrada,"r",encoding = "utf-8") as fichero:
    lineas = fichero.readlines()

lineas_numeradas = []

for i,linea in enumerate(lineas, start = 1):
    linea_numerada = f"{i:04d}: " + linea
    lineas_numeradas.append(linea_numerada)

with open(ruta_salida, "w", encoding = "utf-8") as fichero:
    fichero.writelines(lineas_numeradas) # pegamos la lista de lineas

print(f"Resultados guardados en: {ruta_salida}")
