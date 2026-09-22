"""
    Día 72 - Minutos por actividad
    
    Con pandas, agrupar por actividad y sumar minutos

    Salida: 
    alemán: 105
    python: 20

    Extra: anyadir columna de horas
"""

import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "actividades.csv"
ruta = OUTPUT_DIR / nombre
nombre_nuevo = "actividades_horas.csv"
ruta_salida = OUTPUT_DIR / nombre_nuevo

df = pd.read_csv(ruta)
print(df)

# Creamos un DataFrameGroupBy
por_actividad = df.groupby("actividad")
# esto es un Series
resultado = por_actividad["minutos"].sum()
# si lo quisieramos como diccionario hacemos
dic_resultado = resultado.to_dict()
print(resultado)
print(type(resultado))
print(dic_resultado)

# anyadimos columna horas
df["horas"] = (df["minutos"]/60).round(2)

# guardamos el nuevo df
df.to_csv(ruta_salida, index = False)

df2 = pd.read_csv(ruta_salida)
print(df2)

