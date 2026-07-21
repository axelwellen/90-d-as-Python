# Checkpoint: Analizador de logs v1
#
# Crear: python dia_49.py access.log
#
# debe mostrar: 
# - total de lineas
# - total de IPs
# - códigos HTTP
# - rutas sospechosas
# - eventos de error

from pathlib import Path
import sys

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = sys.argv[1]
ruta_entrada = OUTPUT_DIR / nombre

sospechosas = ["/admin", "/wp-admin", "/login", "/config", "/.env"]

with open(ruta_entrada, "r", encoding = "utf-8") as fichero:
    lineas = fichero.readlines()

print("Total de líneas:",len(lineas))

codigos = {}
rutas_sospechosas = {}
ips = {}
eventos_error = 0

for linea in lineas: 
    elementos = linea.split()
    
    ip = elementos[0].strip()
    metodo = elementos[1].strip()
    ruta = elementos[2].strip()
    codigo = elementos[-1].strip()
    
    ips[ip] = ips.get(ip,0) + 1
    codigos[codigo] = codigos.get(codigo,0) +1
    if 400 <= int(codigo) < 600:
        eventos_error += 1
    if ruta in sospechosas:
        rutas_sospechosas[ruta] = rutas_sospechosas.get(ruta,0) + 1

print("Las IPs con más eventos son:")
top_3 = sorted(ips.items(), key = lambda item:item[1], reverse = True)[:3]
for ip in top_3:
    print(ip[0],"->",ip[1],"veces")
print("Los diferentes códigos HTTP:")
for codigo, veces in codigos.items():
    print(codigo,"->", veces)
print("Las rutas sospechosas existentes son:", rutas_sospechosas)
for ruta_sospechosa,veces in rutas_sospechosas.items():
    print(ruta_sospechosa,"->",veces)
print("Eventos de error:", eventos_error)
