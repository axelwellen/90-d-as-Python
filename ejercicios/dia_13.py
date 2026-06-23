# Detector de permisos

# tenemos que comprobar si el usuario tiene permisos suficientes: 
# Extra: Mostrar qué permisos faltan

permisos_usuario = {"read", "write"}
permisos_requeridos = {"read", "write", "delete"}

def mostrar_permisos(usuario, requeridos):
    # Si el usuario tiene permisos suficientes: True
    # Si no tiene permiso suficientes: False
    permisos_suficientes = requeridos.issubset(usuario)
    permisos_faltantes = requeridos.difference(usuario)
    return {
            "permisos_suficientes":permisos_suficientes,
            "permisos_faltantes":permisos_faltantes 
            }

if __name__ == "__main__":
    permisos = mostrar_permisos(permisos_usuario,permisos_requeridos)
    print(permisos)
