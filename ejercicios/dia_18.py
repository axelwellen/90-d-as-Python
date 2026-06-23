# Función normalizadora
#
# Crear una función que: 
# - quite espacios extra (replace y split)
# - pase a minúsculas (lower())
# - elimine puntos y comas (replace)
# - devuelva el texto limpio (return)
# Extra, usarla en el ejercicio del día 17

def normalizar_texto(texto):
    return " ".join(texto.replace(".","").replace(",","").lower().split())

if __name__ == "__main__":
    texto = "Hola, parece que   ahora sí que sustiuimos todo correctemente? "
    texto_normalizado = normalizar_texto(texto)
    print(texto_normalizado)
