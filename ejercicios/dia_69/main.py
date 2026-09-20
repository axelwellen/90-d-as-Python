"""
    Día 69 - paquete simple

    creamos una estructura de paquete para importar algunas funciones desde el main y poder utilizarlas
"""
from mi_toolkit import is_email, count_words, reverse_text, is_empty

texto = "hola este es un simple texto para contar las palabras"
texto2 = "este es el texto qué irá del revés"
texto3 = "este texto dirá que no está vacío"
texto4 = "    "
texto5 = "mail@hola.com"

print("Contamos las palabras de ->", texto, "->", count_words(texto))
print("Damos la vuelta al texto ->", texto2, "->", reverse_text(texto2))
print("El texto ->", texto3, "está vacío =", is_empty(texto3))
print("El texto ->", texto4, "está vacío =", is_empty(texto4))
print("El texto ->", texto5, "es un mail =", is_email(texto5))



