# Registro de hábitos
# 
# Dada una lista, calcular los minutos totales por activiad
# Extra: convertir minutos a horas


def calcular_tiempo_total(habitos):
    actividades = {}
    for habito in habitos:
        # si la actividad existe sumar minutos, sino, crear y añadir los minutos
        tiempo_total = actividades.get(habito["actividad"],0) + habito["min"]
        actividades[habito["actividad"]]=tiempo_total
    return actividades

def convertir_a_horas(actividades):
    horas = {}
    for actividad,minutos in actividades.items():
        horas[actividad] = round(minutos/60,2)
    return horas

if __name__ == "__main__":
    
    habitos = [
            {"día":"lunes", "actividad":"aleman", "min":60},
            {"día":"lunes", "actividad":"python", "min":20},
            {"día":"martes", "actividad":"aleman", "min":45},
            {"día":"miércoles", "actividad":"aleman", "min":60},
            ]
    actividades = calcular_tiempo_total(habitos)
    print(actividades)
    actividades_horas = convertir_a_horas(actividades)
    print(actividades_horas)
