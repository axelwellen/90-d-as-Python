# Clasificador HTTP desde terminal
#
# usar dia_31.py 404
# La salida será 404 -> error cliente
# Extra, permitir varios códigos
# dia_31.py 200 301 404 500

import sys
from dia_04 import clasificar_codigo
if len(sys.argv) > 1:
    codigos = sys.argv[1:]
    for codigo in codigos:
        if codigo.isdigit():
            print(codigo,"->",clasificar_codigo(int(codigo)))
        else:
            print(codigo,"-> No es un número. Los códigos deben ser números entre 200 y 599")
else:
    print("El formato es incorrecto\n\tpython dia_31.py [código_1] [código_2] ...")
