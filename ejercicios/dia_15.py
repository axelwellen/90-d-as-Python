# Mini diccionario alemán
#
# pedir una palabra y mostrar su traducción

vocabulario = {
            "obwohl":"aunque", 
            "trotzdem":"sin embargo",
            "die Voraussetzung":"requisito"
            }

palabra = input("La traducción de qué palabra quieres ver: ")
if palabra in vocabulario:
    print(vocabulario[palabra])
else:
    traduccion = input("La palabra no existe, introduce traducción para añadir al diccionario: ")
    vocabulario[palabra] = traduccion
print(vocabulario)
