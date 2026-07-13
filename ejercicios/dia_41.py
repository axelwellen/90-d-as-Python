# Separador de errores
# 
# Dado un archivo de logs, separar
# - lineas con ERROR -> errores.txt
# - lineas con WARNING -> warnings.txt
# - resto -> otros.txt

from pathlib import Path

OUTPUTS_DIR = Path(__file__).resolve().parent.parent / "outputs"
ruta_entrada = OUTPUTS_DIR / "logs.txt"
ruta_errores = OUTPUTS_DIR / "errores.txt"
ruta_warnings = OUTPUTS_DIR / "warnings.txt"
ruta_otros = OUTPUTS_DIR / "otros.txt"



with open(ruta_entrada, "r", encoding = "utf-8") as fichero:
    lineas = fichero.readlines()

warnings = []
errores = []
otros = []

for linea in lineas:
    linea_minusc = linea.lower()
    if "error" in linea_minusc:
        errores.append(linea)
    elif "warning" in linea_minusc:
        warnings.append(linea)
    else:
        otros.append(linea)

if warnings:
    with open(ruta_warnings, "w", encoding = "utf-8") as fichero:
        fichero.writelines(warnings)

if errores:
    with open(ruta_errores, "w", encoding = "utf-8") as fichero:
        fichero.writelines(errores)

if otros:
    with open(ruta_otros, "w", encoding = "utf-8") as fichero:
        fichero.writelines(otros)

