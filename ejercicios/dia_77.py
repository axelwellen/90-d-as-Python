"""
    Día 77 - Checkpoint: Dashboard simple

    Crear un script que permita: 
    python dia_77.py habitos.csv

    - Leer CSV
    - Mostra resumen
    - Generar gráfico
    - Guardad reporte
"""
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# leer csv indicando ruta por terminal
if len(sys.argv) == 2:
    ruta = Path(sys.argv[1])
else:
    print("El formato debe ser 'dia_77.py [ruta_del_archivo_csv]'")
    exit()
df = pd.read_csv(ruta, parse_dates=["fecha"])

# *** mostrar resumen por el terminal ***
print(df)

# total por actividad
por_actividad = df.groupby("actividad")["minutos"].sum()
print(por_actividad)

# total por fecha
por_fecha = df.groupby("fecha")["minutos"].sum()
print(por_fecha)

# media diaria
media_diaria = por_fecha.mean()
print(media_diaria) 

# por fecha y actividad
por_fecha_actividad = df.groupby(["fecha","actividad"])["minutos"].sum().unstack(fill_value=0)
print(por_fecha_actividad)

colores = {
        "lectura":"tab:blue",
        "inglés":"orange",
        "programar":"tab:red",
        "alemán":"olive",
        "IAACS":"yellow",
        "Pr":"green",
        "SPSD":"gray",
        "SS":"purple"
        }
colores_grafico = [
        colores.get(actividad,"tab:gray")
        for actividad in por_fecha_actividad.columns
        ]

# total por cuatrimestre
#df[df["fecha"].between("2026-09-01","2027-01-31")]


ruta_imagen = ruta.resolve().parent.parent.parent / "NASVault/gráfico.png"

# generar gráfico
ax = por_fecha_actividad.plot(kind="bar", stacked=True, color= colores_grafico)
ax.set_xticklabels([fecha.strftime("%d-%m") for fecha in por_fecha_actividad.index], rotation=0)
plt.xlabel("Fecha")
plt.ylabel("Minutos")
plt.title("Tiempo por actividad")
plt.tight_layout()
plt.savefig(ruta_imagen)
plt.close()

# guardar reporte .txt en el directorio del archivo
# tiempo total, media diaria, actividad principal
with open(ruta.resolve().parent.parent.parent / "NASVault/reporte.md", "w", encoding = "utf-8") as fichero: 
    fichero.write("# Dashboard de hábitos\n\n")
    
    fichero.write("## Resumen\n\n")
    fichero.write(f"Tiempo medio diario: =={media_diaria:.2f}== minutos\n\n")
    
    fichero.write("## Tiempo por actividad\n\n")
    fichero.write(por_actividad.to_frame("minutos").to_markdown())
    fichero.write("\n\n")

    fichero.write("## Gráfico")
    fichero.write(f"![[{ruta_imagen.name}]]\n\n")
    
    fichero.write("## Lista actividades\n\n")
    fichero.write(df.to_markdown(index=False))
#    fichero.write("Media diaria" + media_diaria)
print("Fichero generado")

