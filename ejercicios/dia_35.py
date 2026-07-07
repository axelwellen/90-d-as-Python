# Toolkit terminal
# uso: python dia_35.py [acción] [argumentos] ...
# acciones posibles: 
#     saludo
#     http
#     ip
# ejemplo: python dia_35.py http 404

import sys
import subprocess

mensaje = "Formato incorrecto! Debe ser:\npython dia_35.py [acción] [argumentos]\nAcciones posibles: saludo, http, ip"
if len(sys.argv) < 2:
    print(mensaje)
    exit()

comando = ["python3"]
match sys.argv[1]:
    case "saludo":
        comando.append("dia_29.py")
    case "http":
        comando.append("dia_31.py")
    case "ip":
        comando.append("dia_34.py")
    case _:
        print(mensaje)
        exit()
if len(sys.argv) > 2:
    comando.extend(sys.argv[2:])
subprocess.run(comando)
