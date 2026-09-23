"""
    Día 74 - Gráfico simple

    Usar matplotlib para crear un gráfico de barras con minutos por actividad

    Extra: guardar el gráfico como gráfico.png

"""
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre = "actividades.csv"
imagen = "grafico.png"
ruta = OUTPUT_DIR /nombre
ruta_imagen = OUTPUT_DIR / imagen

df = pd.read_csv(ruta)
print(df)

por_actividad = df.groupby("actividad")["minutos"].sum()
print(por_actividad)
por_actividad.plot(kind="bar")
plt.xlabel("Actividad")
plt.ylabel("Tiempo (minutos)")
plt.title("Tiempo por actividad")

# guardamos la imagen (para que no se corte usamos tight_layout
plt.tight_layout()
plt.savefig(ruta_imagen)
plt.show()


