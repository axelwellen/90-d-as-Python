""" 
    Mini checkpoint: generador + analizador
    Scritp que:
    - genere logs simulados
    - los guarde en archivo
    - los lea
    - muestre top IPs con más fallo
"""

import random
from pathlib import Path
from collections import Counter

usr_ini = ["Ba","Be","Da","De","Ka","La","Ma","Me","Pa","Ra","Ta","Va","Za"]
usr_med = ["la","le","ra","re","sa","se","ta","va","mi","ne"]
usr_fin = ["na","ra","sa","ta","nia","lia","mir","an","or","va","te","za","nel","son"]
resultados = ["ok", "failed"]
ips = []
nombres = []
eventos = []

for i in range(2500):
    ip = str(random.randint(250,254)) # acotamos para que se repitan
    nombre = random.choice(usr_ini) + random.choice(usr_med) + random.choice(usr_fin)
    nombres.append(nombre)
    resultado = random.choice(resultados)
    for i in range(3):
        ip += "." + str(random.randint(250,254))
    ips.append(ip)
    evento = f"{ip} - {nombre} login attempt {resultado}\n"
    eventos.append(evento)

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "login_simulado.log"
ruta = OUTPUT_DIR / name

with open(ruta, "w", encoding = "utf-8") as fichero:
    fichero.writelines(eventos)

# Ahora leemos el archivo en lugar de utilizar la info que ya tenemos

with open(ruta, "r", encoding = "utf-8") as fichero: 
    lineas = fichero.readlines()

resumen = Counter()

for linea in lineas:
    ip = linea.split("-")[0].strip()
    usr = linea.split(" ")[2].strip()
    event = linea.strip().split(" ")[-1]
    if event == "failed":
        resumen.update([ip])

for ip, fallos in resumen.most_common(5):
    print(ip, "->", fallos, "fallos")

