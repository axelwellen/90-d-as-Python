import requests

# nota: Se podrían manejar erores de la API, como el no tener internet o el formato esperado. 
url = "https://api.open-meteo.com/v1/forecast"

params = {
        "latitude": 49.0069,
        "longitude": 8.4037,
        "current": "temperature_2m"
        }

res = requests.get(url, params = params)
data = res.json()

temp = data["current"]["temperature_2m"]

while True:
    try: 
        opcion = int(input(f"Temperatura actual: {temp} °C\n- Opción 1: Convertir temperatura a Fahrenheit\n- Opción 2: Convertir temperatura a Kelvin\nIntroduce una opción: "))
    except ValueError: 
        print("El valor introducido debe ser '1' o '2'")
        continue
    match opcion: 
        case 1:
            temperatura = temp * 9/5 + 32
            print(temperatura, "°F")
            break
        case 2:
            temperatura = temp + 273.15
            if temperatura < 0:
                print("La temperatura por debajo de 0 grados Kelvin no es posible")
                break
            else:
                print(temperatura, "K")
                break
        case _:
            print("El valor introducido debe ser '1' o '2'")
