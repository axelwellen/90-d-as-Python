"""
    Día 68 - Módulo propio de utilidades

    Crear utils.py con funciones: 

    - normalizar_texto
    - leer_entero
    - validar_ip
    - es_password_segura
"""

def normalizar_texto(texto): 
    return " ".join(texto.replace(".","").replace(",","").lower().split())

def leer_entero(mensaje):
    """
        Esta función pide un número entero al usuario hasta que el usuario lo introduce bien
    """
    while True:
        try: 
            return int(input(mensaje))
        except ValueError:
            print("Debes introducir un número entero")

def validar_ip(ip): 
    ip_list = ip.split(".")
    if len(ip_list) == 4: 
        for seg in ip_list:
            if not seg.isdigit():
                return False
            else:
                if not 0 <= int(seg) <= 255:
                    return False
        return True
    else:
        return False

def es_password_segura(psw):
    tam = len(psw) >= 8
    low = any(c.islower() for c in psw) # si alguno es mayusc -> True
    upper = any(c.isupper() for c in psw) 
    num = any(c.isdigit() for c in psw)
    simb = any(c in "!#$%" for c in psw)
    if tam and upper and low and num and simb:
        return True
    return False

if __name__ == "__main__": 
    texto = " Este es  el TEXTo   a Normalizar  ,  a ver que tal   "
    ip = "192.168.127.3"
    psw = "estaEs736355#"

    if validar_ip(ip):
        print(f"La IP {ip} es válida")
    else:
        print(f"La IP {ip} no es válida")

    print(normalizar_texto(texto))

    if es_password_segura(psw):
        print("La contrasenya es segura")
    else: 
        print("La contrasenya no es segura")

    opcion = leer_entero("Selecciona una opcion: ")
