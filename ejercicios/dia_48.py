# Eventos por severidad
# 
# Dado un archivo como system.log
# Contar eventos por severidad
# Extra: mostrar solo los de severidad alta

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "system.log"
ruta = OUTPUT_DIR / nombre

with open(ruta, "r", encoding = "utf-8") as fichero:
    lineas = fichero.readlines()

eventos = {}

for linea in lineas: 
    evento = linea.split()[0].strip()
    eventos[evento] = eventos.get(evento,0) + 1

eventos_severidad = {"CRITICAL", "ERROR"}

for evento, veces in eventos.items():
    if evento in eventos_severidad:
        print(evento,"ha sucedido",veces,"veces")

