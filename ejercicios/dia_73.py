""" 
    Día 73 - Minutos por día

    Agrupar por día y calcular tiempo total estudiado cada día

    Extra: detectar el día con más minutos
"""

import pandas as pd
from pathlib import Path
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "actividades.csv"
ruta = OUTPUT_DIR / nombre

df = pd.read_csv(ruta)
print(df)

por_dia = df.groupby("dia")
tiempo = por_dia["minutos"].sum()
print(tiempo)

# día con más minutos
dia_max = tiempo.idxmax() # index where the maximum is
tiempo_max = tiempo.max() # maximum value
print("El tiempo máximo fue el", dia_max, "con un tiempo total de", tiempo_max)
