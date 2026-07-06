# Validador de IP desde terminal
# uso: python dia_34.py 192.168.1.10
# salida: IP válida
# Extra: permitir validar varias IPs de golpe
from dia_25 import es_ip_valida
import sys

ips = sys.argv[1:]
if not ips:
    print("El formato es python dia_34.py [ip_1] [ip_2] ...")
for ip in ips:
    if es_ip_valida(ip):
        print("IP",ip,"válida")
    else:
        print("IP",ip,"no válida")


