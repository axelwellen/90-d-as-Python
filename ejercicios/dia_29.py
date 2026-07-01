# Hola terminal
#
# Crear un script que ejecutemos como python dia_29.py Axel
# Y que la salida sea Hola, Axel

import sys

if len(sys.argv) == 2:
    nombre = sys.argv[1]
    print("Hola,", nombre)
else: 
    print("Para ejecutar el script escribir 'python dia_29.py [Nombre]'")

