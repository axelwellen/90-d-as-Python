""" 
    Día 76 - Analizador de hábitos

    Leer un CSV de hábitos y mostrar: 

    - Total por actividad
    - Media diaria
    - Mejor día
    - Peor día

    Extra: generar gráfico
"""

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
name = "actividades.csv"
imagen = "actividades_dia.png"
ruta_imagen = OUTPUT_DIR / imagen
ruta = OUTPUT_DIR / name

# para ordenar por día de la semana
df = pd.read_csv(ruta)
orden_dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
df["dia"] = pd.Categorical(df["dia"], categories=orden_dias, ordered = True)
print(df)

# Mostrar total de tiempo por actividad
por_actividad = df.groupby("actividad")["minutos"].sum()
print("*** TOTAL TIEMPO POR ACTIVIDAD ***")
print(por_actividad)

# Mostrar media diaria
por_dia = df.groupby("dia", observed = False)["minutos"] # le dice a Pandas que tengamos en cuenta las categorías definidas
print("*** ESTADÍSTICAS ***")
print("El tiempo medio por día es de",por_dia.sum().mean().round(2), "minutos")

# Mostrar mejor día
mejor_dia = por_dia.sum().idxmax()
mejor_tiempo = por_dia.sum().max()
print("El mejor día fue el",mejor_dia,"con un tiempo total de", mejor_tiempo)

# Mostrar peor día
peor_dia = por_dia.sum().idxmin()
peor_tiempo = por_dia.sum().min()
print("El peor día fue el", peor_dia, "con un tiempo total de", peor_tiempo)

# Generar gráfico de barras
#por_dia.sum().plot(kind="bar")
#plt.xlabel("Día")
#plt.ylabel("Minutos")
#plt.title("Tiempo por actividad")

#plt.tight_layout()
#plt.savefig(ruta_imagen)
#plt.show()

# Generar gráfico de barras apiladas
por_dia_actividad = df.groupby(["dia","actividad"], observed=False)["minutos"].sum().unstack(fill_value=0) # unstack convierte el segundo nivel (actividad) en columnas
print(por_dia_actividad)
por_dia_actividad.plot(kind="bar", stacked=True)
plt.xlabel("Día")
plt.ylabel("Minutos")
plt.title("Tiempo por actividad")
plt.tight_layout()
plt.savefig(ruta_imagen)
plt.show()
