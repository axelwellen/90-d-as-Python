# Simulador de intentos de login
#
# Generar 30 eventos aleatorios con:
# - IP aleatoria
# - usuario aleatorio
# - resultado ok y failed
# Guardarlos en login_simulado.log
# Extra: analizar que IP falló más

import random
from pathlib import Path

usr_ini = ["Ba","Be","Da","De","Ka","La","Ma","Me","Pa","Ra","Ta","Va","Za"]
usr_med = ["la","le","ra","re","sa","se","ta","va","mi","ne"]
usr_fin = ["na","ra","sa","ta","nia","lia","mir","an","or","va","te","za","nel","son"]
resultados = ["ok", "failed"]
ips = []
nombres = []
eventos = []

for i in range(30):
    ip = str(random.randint(1,254))
    nombre = random.choice(usr_ini) + random.choice(usr_med) + random.choice(usr_fin)
    nombres.append(nombre)
    resultado = random.choice(resultados)
    for i in range(3):
        ip += "." + str(random.randint(1,254))
    ips.append(ip)
    evento = f"{ip} - {nombre} login attempt {resultado}\n"
    eventos.append(evento)

print(ips)
print(nombres)
print(eventos)

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "login_simulado.log"
ruta = OUTPUT_DIR / name

with open(ruta, "w", encoding = "utf-8") as fichero:
    fichero.writelines(eventos)


