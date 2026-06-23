# Contador de palabras

# dado un texto: 
# contar el número de veces que aparece cada palabra
# ignorar mayúsculas, comas/puntos

texto = "error login failed error user denied login error"

def contar_palabras(texto):
    texto_lista = texto.replace("."," ").replace(","," ").lower().split()
    diccionario_palabras = {}

    for elem in texto_lista:
        if elem in diccionario_palabras:
            diccionario_palabras[elem] += 1
        else:
            diccionario_palabras[elem] = 1
    return diccionario_palabras
if __name__ == "__main__":
    diccionario_palabras = contar_palabras(texto)
    for clave, valor in diccionario_palabras.items():
        print(clave,"-->", valor)



