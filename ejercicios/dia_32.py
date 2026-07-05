# Buscador de palabra en frase
# dia_32.py "login failed for admin" failed
# Debe decir si aparece la palabra y cuantas veces aparece

import sys
from dia_03 import contar_palabras

if len(sys.argv) == 3:
    texto = sys.argv[1]
    palabra = sys.argv[2].lower() # contar_palabras pasa todo a minúscula
    cantidad = contar_palabras(texto).get(palabra,0) # devuelve el número de veces que aparece palabra
    print(palabra,"aparece",cantidad,"veces")
else:
    print('El formato debe ser python dia_32.py "texto donde buscar las palabras" [palabra]')

