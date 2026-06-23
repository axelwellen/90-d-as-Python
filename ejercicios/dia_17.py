# Agrupador por primera letra
# 
# Dada una lista de palabras, agruparlas por la primera letra en diccionarios
# Extra: Ignorar mayúsculas/minúsculas
from dia_18 import normalizar_texto

palabras = ["Haus", "Hund", "Auto", "Arbeit", "Zeit", "hola", "haus", "zeit", "zeit", "Büro", "büro"]

def agrupar_palabras(palabras):
    dic = {}
    for palabra_raw in palabras:
        palabra = normalizar_texto(palabra_raw)
        inicial = palabra[0].upper()
        if inicial in dic:
            if palabra.capitalize() in dic[inicial]:
                continue
            else:
                dic[inicial].append(palabra.capitalize())
        else:
            dic[inicial] = [palabra.capitalize()]
    return dic

if __name__ == "__main__":
    palabras_agrupadas = agrupar_palabras(palabras)
    print(palabras_agrupadas)
