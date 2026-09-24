"""
    Día 75 - NumPy básico

    crear un array de notas o minutos
    datos = np.array([20, 30, 45, 60, 10])

    Calcular: 
    - media
    - máximo
    - mínimo
    - desviación estándar

    Extra: generar 30 valores aleatorios simulando minutos diarios
"""

import numpy as np

#datos = np.array([20,30,45,60,10])
datos = np.random.randint(61, size=30)
print(datos)

print("La media del array es:", datos.mean())
print("El valor máximo del array es:", datos.max())
print("El valor mínimo del array es:", datos.min())
print("La desviación estandar del array es:", round(datos.std(),2))
