# Reporte semanal 
# Crear un reporte semanal a partir del diccionario de habitos que tenemos creado en el día 20
# Extra: Guardar el reporte en "reporte.txt"
from dia_20 import convertir_a_horas, calcular_tiempo_total
from pathlib import Path

def crear_reporte(habitos):
    actividades = convertir_a_horas(calcular_tiempo_total(habitos))
    reporte = "Reporte semanal\n----------------\n"
    for actividad, horas in actividades.items():
        reporte += f"{actividad}: {horas} horas\n"
    return reporte

def guardar_reporte(reporte, ruta):
    with open(ruta, "w", encoding = "utf-8") as fichero:
        fichero.write(reporte)

if __name__ == "__main__":
    habitos = [
        {"día":"lunes", "actividad":"aleman", "min":60},
        {"día":"lunes", "actividad":"python", "min":20},
        {"día":"martes", "actividad":"aleman", "min":45},
        {"día":"miércoles", "actividad":"aleman", "min":60},
        ]
    
    OUTPUTS_DIR = Path(__file__).resolve().parent.parent / "outputs"
    ruta_reporte = OUTPUTS_DIR / "reporte_dia_21.txt"
    reporte = crear_reporte(habitos)
    print(reporte)
    guardar_reporte(reporte, ruta_reporte)
