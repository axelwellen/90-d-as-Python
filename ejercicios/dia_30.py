# Suma desde terminal
#
# usar dia_30.py 4 7 
# salida 4 +7 = 11
# Extra controlar que los argumentos sean números
# Nota: isdigit solo sirve para enteros positivos, sino hay que usar try/except
import sys

if len(sys.argv) == 3:
    num_1 = sys.argv[1]
    num_2 = sys.argv[2]
    if num_1.isdigit() and num_2.isdigit():
        print(num_1,"+",num_2,"=",int(num_1) + int(num_2))
    else:
        print("El formato debe ser dia_30.py [número] [número]")
else:
    print("El número de términos no es correcto: (Ej: dia_30.py 4 7)\nSalida --> 4 + 7 = 11")
