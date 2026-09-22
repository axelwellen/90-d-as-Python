""" 
    Día 71 - Leer CSV con pandas

    Crear un CSV:
    dia, actividad, minutos
    lunes, alemán, 60
    lunes, python, 20
    martes, alemán, 45
    
    Leerlo con pandas y mostrarlo

    Extra: mostrar solo activades de alemán
"""

import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "actividades.csv"
ruta = OUTPUT_DIR / nombre

# leemos el csv y lo printamos
df = pd.read_csv(ruta)
print(df)

# Ahora trabajamos con el dataframe, vamos a mostrar solo las actividades de alemán
print("Mostramos solo las actividades de alemán:")
print(df[df["actividad"]=="alemán"])
