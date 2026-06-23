# buscador de palabra en frase

# Pedir una frase y una palabra y mostrar: 
# si aparece la palabra
# cuántas veces aparece
# primera posición
# última posición
# Extra: que no importen mayúsculas y minusculas


def buscador_palabra_frase(frase, palabra):
    frase_min = frase.lower()
    palabra_min = palabra.lower()

    if palabra_min in frase_min:
        total = frase_min.count(palabra_min)
        prim = frase_min.find(palabra_min)  
        print("La palabra",palabra,"aparece en la frase",total,"veces. La primera posición es la",prim, end=" ")
        if total > 1:
            ult = frase_min.rfind(palabra_min)
            print("y la última posición es la",ult)
    else: 
        print("La palabra",palabra,"no aparece en la frase")

if __name__ == "__main__":
    frase = input("introduce una frase: ")
    palabra = input("introduce una palabra: ")
    buscador_palabra_frase(frase, palabra)
