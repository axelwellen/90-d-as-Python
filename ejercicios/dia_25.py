# Validador de IP simple
# 
# Pedir una IP y comprobar que: 
# - Tiene 4 partes
# - Todas son números
# - cada número está entre 0 y 255
# Extra: Convertirlo en función es_ip_valida(ip)

def es_ip_valida(ip):
    ip_list = ip.split(".")
    if len(ip_list) == 4:
        for seg in ip_list:
            if not seg.isdigit():
                #print(seg, "no contiene solo dígitos")
                return False
            else:
                if not 0 <= int(seg) <= 255:
                    #print(seg, "no se encuentra entre 0-255")
                    return False
        return True
    else:
        #print(ip, "no tiene el formato 192.168.1.10")
        return False

if __name__ == "__main__":
    #ip = "192.168.1.10"
    ip = input("Introduce una IP: ")
    print(es_ip_valida(ip))

