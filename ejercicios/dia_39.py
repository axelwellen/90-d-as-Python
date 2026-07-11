# Limpiador de archivo
# 
# Leer: suicio.txt limpiar cada linea con strip() y guardar el resultado en limpio.txt
# Extra: Eliminar líneas vacías
# 

from pathlib import Path

OUTPUTS_DIR = Path(__file__).resolve().parent.parent / "outputs"
ruta = OUTPUTS_DIR / "sucio.txt"
ruta_salida = OUTPUTS_DIR / "limpio.txt"

with open(ruta, "r", encoding = "utf-8") as fichero:
    lineas = fichero.readlines()

lineas_limpias = []
for linea in lineas:
    linea_limpia = linea.strip()
    if linea_limpia: # Si hay algo en la linea, si son espacios o salto de linea, estará vacío después del strip
        lineas_limpias.append(linea_limpia + "\n")

with open(ruta_salida, "w", encoding="utf-8") as fichero:
    fichero.writelines(lineas_limpias)
    
print(f"Resultados guardados en: {ruta_salida}")
