# Generador de contraseñas
#
# Generar una contraseña aleatoria de longitud dada
# Debe incluir: 
# - letras
# - números
# - símbolos
# Extra: premitir elegir longitud por terminal

import sys
import random

longitud = 10

if len(sys.argv) >= 2:
    if sys.argv[1].isdigit():
        longitud = int(sys.argv[1])

letras_may = "QWERTZUIOPASDFGHJKLYXCVBNM"
letras_min = "qwertzuiopasdfghjklyxcvbnm"
simbolos = "_#-$%&!^*+="
numeros = "1234567890"

elementos = [letras_may, letras_min, simbolos, numeros]
psw = ""
# primera versión
for i in range(longitud):
    lista = random.randint(0,3)
    caracter = random.choice(elementos[lista])
    psw += caracter

print(psw)

# alternativa que asegura un elemento de cada
psw2 = ""
for i in range(4):
    psw2 += random.choice(elementos[i])
for i in range(4,longitud):
    lista = random.randint(0,3)
    caracter = random.choice(elementos[lista])
    psw2 += caracter
print(psw2)

# alternativa cortando un string
caracteres = letras_may + letras_min + simbolos + numeros
list_car = list(caracteres)
random.shuffle(list_car)
psw3 = "".join(list_car[:longitud])
print(psw3)
