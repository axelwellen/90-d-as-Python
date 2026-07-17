# Detector de fuerza bruta simple
#
# Si una IP tiene más de 3 eventos failed, marcarla como sospechosa
# salida: IP sospechosa: 192.168.1.10 -> 5 intentos
# Extra: generar reporte en archivo

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "auth.log"
ruta = OUTPUT_DIR / nombre
ruta_salida = OUTPUT_DIR / "reporte_failed.txt"

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

reporte = ""

for failed_ip,veces in eventos["failed"].items():
    if veces > 3:
        reporte += f"IP sospechosa: {failed_ip} -> {veces} intentos\n"

print(reporte)
with open(ruta_salida, "w", encoding = "utf-8") as fichero:
    fichero.write(reporte)

print("Reporte guardado en", ruta_salida)
