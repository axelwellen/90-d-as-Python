# Contador de IPs en logs
#
# Dada una lista o archivo con lineas con IPs y eventos del estilo: 
# 192.168.1.10 - login failed
# Contar eventos por IP
# Extra: Mostrar el top 3 IPs

from pathlib import Path

# lo primero será leer el archivo
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "auth.log"
ruta = OUTPUT_DIR / nombre

with open(ruta,"r", encoding = "utf-8") as fichero: 
    lineas = fichero.readlines()

ips = {}
for linea in lineas: 
    ip = linea.split("-")[0].strip()
    veces = ips.get(ip,0)
    ips[ip] = veces + 1


for ip,veces in ips.items():
    print(ip,"->", veces)

top_3 = sorted(ips.items(), key= lambda item: item[1], reverse = True)[:3]

print(top_3)

for ip, veces in top_3:
    print(ip,"->", veces)
