# Días hasta una fecha
#
# Pedir una fecha objetivo y calcular cuántos días faltan
# 01-09-2026 
# Extra: calcular cuantas semanas también

import sys
import datetime

if len(sys.argv) == 2:
    fecha = sys.argv[1].split("-")

    dia = int(fecha[0])
    mes = int(fecha[1])
    anyo = int(fecha[2])
    
    fecha_objetivo = datetime.date(anyo,mes,dia)
    fecha_actual = datetime.date.today()
    
    diferencia = fecha_objetivo - fecha_actual
    dias = diferencia.days
    #print(type(diferencia))
    #print(dir(diferencia))
    #print(help(diferencia))
    
    if dias >= 0:
        print(f"Faltan {dias} días")
    else: 
        print(f"Han pasado {abs(dias)} días") 
    
    semanas = abs(dias)/7
    print(f"Que son {semanas:.1f} semanas")
else: 
    print("Formato incorrecto, debes introducir:\npython dia_50.py [fecha en formato dd-mm-aaaa]")
