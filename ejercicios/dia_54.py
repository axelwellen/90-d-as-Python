# Counter de palabras
# 
# Usar collections.Counter para contar palabras de un texto (no números ni símbolos)
# Extra: mostrar las 5 más comunes

from collections import Counter
from pathlib import Path
import re

INPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "login_simulado.log"
ruta = INPUT_DIR / name

with open(ruta, "r", encoding = "utf-8") as fichero:
    lineas = fichero.readlines()

palabras = Counter()
for linea in lineas: 
    linea = linea.strip().lower()
    linea = re.sub(r"[^a-züöäß\s]","",linea) # quitamos todos los símbolos raros
    #palabras += Counter(linea.split())
    palabras.update(linea.split())

print("Todas las palabras:", palabras)
print("Las 5 palabras más comunes:")
for palabra, veces in palabras.most_common(5):
    print(palabra,"->",veces,"veces")
