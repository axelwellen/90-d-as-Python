# Parser de línea de log
#
# Dada una línea del estilo: 
# 192.168.1.10 - admin - login failed
# Extraer la IP, usuario, evento
# Extra: Si la línea no tiene el formato correcto, mostrar el error controlado

from dia_25 import es_ip_valida

def extraer_datos(linea):
    info = linea.split(" - ")
    if len(info) != 3:
        print("El formato introducido no es correcto, ha de ser: ip - usuario - evento")
        return None
    if not es_ip_valida(info[0]):
        print("La IP no es válida")
        return None
    if not info[1]:
        print("El usuario no puede estar vacío")
        return None
    if not info[2]:
        print("El evento no puede estar vacío")
        return None
    return {
            "ip":info[0].strip(),
            "usuario":info[1].strip(),
            "evento":info[2].strip()
            }

if __name__ == "__main__":
    linea = "192.168.1.10 - admin - login failed"
    datos = extraer_datos(linea)
    print(datos)
