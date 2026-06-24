# Lector seguro de números
# 
# Crear la función: leer_entero(mensaje)
# Debe pedir un número hasta que el usuario introduzca un entero válido
# Extra: permitir valor mínimo y máximo

def leer_entero(mensaje, rango_inferior = None, rango_superior = None):
    # Vamos a hacer la prueba de un docstring, para cuando trabajemos en un IDE
    """
    Pide al usuario un número entero hasta que introduzca uno válido.

    Args:
        mensaje (str): Texto que se muestra al perid el número.
        rango inferior (int, optional): Valor mínimo permitido.
        rango_superior (int, optional): Valor máximo permitido.

    Returns: 
        int: Número entero válido introducido por el usuario.
    """
    while True: 
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("La opción introducida debe ser un número entero!")
            continue
        if rango_inferior is not None and numero < rango_inferior:
            print("El número está por debajo del rango inferior permitido!")
            continue
        if rango_superior is not None and rango_superior < numero:
            print("El número está por encima del rango superior permitido!")
            continue

        print("Número elegido:",numero)
        return numero

if __name__ == "__main__":
    rango_inferior = 1
    rango_superior = 100
    mensaje = f"Introduce un número entre {rango_inferior} y {rango_superior}: " 
    numero = leer_entero(mensaje, rango_inferior, rango_superior)
