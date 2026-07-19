# Analizador de c#odigos HTTP
#
# Dado un archivo access.log con lineas tipo: 
# 192.168.1.10 GET /login 200
# 192.168.1.11 GET /admin 403
# Contar los códigos HTTP
# Extra: Separar los 2xx,3xx,4xx,5xx.

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "access.log"
ruta = OUTPUT_DIR / nombre

with open(ruta,"r", encoding = "utf-8") as fichero:
    lineas = fichero.readlines()

codigos = {}

for linea in lineas: 
    vector_linea = linea.split()
    ip = vector_linea[0].strip()
    codigo = int(vector_linea[-1].strip())

    if codigo not in codigos:
        codigos[codigo] = {} # si no existe el codigo, lo creamos
    
    codigos[codigo][ip] = codigos[codigo].get(ip,0) + 1 # si no existe la IP devuelve 0, sino el número de veces. En ambos sumamos 1. 

for codigo,ips in codigos.items():
    for ip,veces in ips.items(): 
        print(codigo,"->",ip,"-",veces,"veces")
