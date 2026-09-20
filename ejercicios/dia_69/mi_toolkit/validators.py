# funcion para validar un mail
def is_email(text):
    """
    Devuelve True si tenemos una '@' y un punto en el texto indicado
    """
    return "@" in text and "." in text

# función para ver si un texto está vacío
def is_empty(text):
    """
    Si hay algo después de hacer strip, devuelve True
    Si no hay nada y está vacío devuelve False
    """
    return not text.strip()
