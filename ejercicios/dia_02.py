# Validador de contraseñas

# Crearemos una función que indique si la contraseña que hemos creado es segura:
# Comprobará:
# - mínimo 8 caracteres -> tam
# - una mayúscula -> upper
# - una minúscula -> low
# - un número -> num
# - un simbolo de !@#$% -> simb
# Extra: imprimir qué regla falla

def es_segura(password):
    tam = len(password)>=8 
    upper = any(c.isupper() for c in password)
    low = any(c.islower() for c in password)
    num = any(c.isdigit() for c in password)
    simb = any(c in "!#$%" for c in password)
    if not tam:
        print("Debe tener por lo menos 8 dígitos")
    if not upper:
        print("Debe tener por lo menos una mayúscula")
    if not low:
        print("Debe tener por lo menos una minúscula")
    if not num:
        print("Debe tener por lo menos un número")
    if not simb:
        print("Debe tener por lo menos un símbolo")
    if tam and upper and low and num and simb:
        print("Contraseña segura")
        return True
    return False

if __name__ == "__main__":
    password =  input("Introduce una contraseña: ")
    es_segura(password)
