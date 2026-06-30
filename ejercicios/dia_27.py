# Menú robusto
# 
# Menú que no se rompa
# 1 saludar, 2 mostrar fecha, 3 salir
# Extra, usar while, try except y funciones
import datetime

def saludar():
    return ("Hola muy buenas")

def fecha():
    dt = datetime.datetime.now()
    return f"{dt.day:02d}/{dt.month:02d}/{dt.year}"

if __name__ == "__main__":
    while True:
        try:
            opcion = int(input("Introduce una opción:\n1) Saludar\n2) Mostrar Fecha\n3) Salir\n-->"))
        except ValueError: 
            print("Debes introducir un número entre 1 y 3")
            continue
        if opcion == 1:
            print(saludar())
            print("Introduce una nueva opción")
        elif opcion == 2:
            print("La fecha es:", fecha())
        elif opcion == 3:
            print("Hasta pronto!")
            break
        else:
            print("Introduce un número entre 1 y 3")

