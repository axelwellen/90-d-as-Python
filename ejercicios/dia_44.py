# Detector de login fallido
#
# Buscar líneas de código que contengan failed, denied o invalid
# Contar cuántos eventos sospechosos hay
# Extra: agrupar por IP
# usaremos auth.log

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "auth.log"
ruta = OUTPUT_DIR / nombre

with open(ruta, "r", encoding = "utf-8") as fichero:
    lineas = fichero.readlines()

eventos = {
        "failed":{},
        "denied":{},
        "invalid":{}
        }

for linea in lineas:
    ip = linea.split("-")[0].strip()
    for evento, ips in eventos.items():
        if evento in linea.lower(): 
            veces = ips.get(ip,0)
            ips[ip] = veces + 1

print(eventos)
