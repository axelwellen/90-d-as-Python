# Rutas sospechosas
#
# detectar peticiones a rutas como: 
# sospechosas = ["/admin", "/wp-admin", "/login", "/config", "/.env"]
# Extra: contar qué IP accede a más rutas sopechosas
# usaremos access.log

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "access.log"
ruta = OUTPUT_DIR / nombre

with open(ruta, "r", encoding = "utf-8") as fichero: 
    lineas = fichero.readlines()

sospechosas = ["/admin", "/wp-admin", "/login", "/config", "/.env"]
ips = {}

for linea in lineas: 
    vector_linea = linea.split()
    ip = vector_linea[0].strip()
    directorio = vector_linea[-2].strip()

    if directorio in sospechosas:
        if ip not in ips:
            ips[ip] = {} # si la ip no está en ips, la creamos
        ips[ip][directorio] = ips[ip].get(directorio, 0) + 1 # si existe nos devuelve el numero, sino 0 y se le suma 1 a ambos casos

sos = {}

for ip,eventos in ips.items():
    eventos_sospechosos = sum(eventos.values()) # se suman todos los valores de la misma ip. Evitamos así hacer un for
    print("La IP", ip, "tiene", eventos_sospechosos,"eventos sospechosos")
    sos[ip] = eventos_sospechosos

top = sorted(sos.items(), key = lambda item:item[1], reverse = True)[0]

print("La IP con más eventos sospechosos es", top[0], "con un total de", top[1], "eventos sospechosos")


