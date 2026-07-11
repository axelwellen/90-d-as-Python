# Guardar resultados
# 
# Modificar el programa dia_37.py
# ejemplo: python dia_38.py error logs.txt
# 

import sys
from pathlib import Path

if len(sys.argv) > 2:
    palabra = sys.argv[1]
    nombre = sys.argv[2]
    OUTPUTS_DIR = Path(__file__).resolve().parent.parent / "outputs"
    ruta_salida = OUTPUTS_DIR / "resultados.txt"
    if len(sys.argv) > 3:
        ruta = Path(sys.argv[3]) / nombre
    else:
        ruta = OUTPUTS_DIR / nombre
else: 
    print("El formato debe ser:\npython dia_37.py [palabra_a_buscar] [nombre_archivo] [(opcional)directorio]")
    exit()

# Si todo está correcto, leemos el archivo y buscamos la palabra en las diferentes líneas. 
with open(ruta, "r", encoding = "utf-8") as fichero:
    lineas = fichero.readlines()
lista_lineas = []
coincidencias = 0
for i, linea in enumerate(lineas, start = 1):
    veces = linea.lower().count(palabra.lower())
    coincidencias += veces
    if veces > 0:
        lista_lineas.append(f"Línea {i}: " + linea) # linea ya contiene \n
        print(f"\033[34m{palabra}\033[0m aparece {veces} veces en la línea {i}")
        print("    ",linea.replace(palabra,f"\033[32m{palabra}\033[0m").strip())
    
with open(ruta_salida, "w", encoding="utf-8") as fichero:
    fichero.writelines(lista_lineas)
    fichero.write(f"\nTotal de coincidencias: {coincidencias}\n")

print(f"Resultados guardados en: {ruta_salida}")
