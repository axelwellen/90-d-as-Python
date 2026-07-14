# Mini grep
# 
# Crear una versión simple de grep:
# ejemplo: python dia_42.py palabra archivo.txt 
# debe: 
#     - leer el archivo
#     - buscar palabra
#     - mostrar número de línea
#     - guardar resultados opcionalmente

from pathlib import Path
import sys

tutorial = """
    Formato para usar mini grep:

    formato: python dia_42.py [palabra_a_buscar] [nombre_del_archivo_donde_buscar]
    * por defecto nombre de salida es "salida_grep.txt"
    parametros:
        -s [nombre_archivo_donde_guardar] (opcional)
        -ro [ruta_origen] (opcional)
        -h or -help (mostrar ayuda)
        -rd [ruta_destino] (opcional)
    """
params = {}
vec_copia = []

for i, elem in enumerate(sys.argv):
    if elem == "-h" or elem == "-help":
        print(tutorial)
        exit()
    if elem == "-s":
        params[elem] = sys.argv[i+1]
        vec_copia.extend(sys.argv[i:i+2])
    if elem == "-ro":
        params[elem] = sys.argv[i+1]
        vec_copia.extend(sys.argv[i:i+2])
    if elem == "-rd": 
        params[elem] = sys.argv[i+1]
        vec_copia.extend(sys.argv[i:i+2])

restante = [e for e in sys.argv if e not in vec_copia] # crea un vector con lo que no hemos guardado en vec_copia
if len(restante) != 3:
    print("El formato introducido no es correcto")
    exit()

palabra = restante[1]
nombre_entrada = restante[2]

# rutas
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
nombre_salida = "salida_grep.txt"
guardar = False

directorio_salida = OUTPUT_DIR
directorio_entrada = OUTPUT_DIR

# -s nombre archivo salida
if params.get("-s",False):
    nombre_salida = params.get("-s")
    guardar = True
# -ro ruta origen
if params.get("-ro",False):
    directorio_entrada = Path(params.get("-ro"))
# -rd ruta destino
if params.get("-rd",False):
    directorio_salida = Path(params.get("-rd"))

ruta_entrada = directorio_entrada / nombre_entrada
ruta_salida = directorio_salida / nombre_salida 

# ya tenemos las rutas del archivo, ahora se trata de abrir el archivo, hacer lo que corresponda y guardar en caso de que corresponda

with open(ruta_entrada, "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
    print("Leído el archivo de la ruta:",ruta_entrada)
lineas_encontradas = []
# buscamos y añadimos el número de linea
for i, linea in enumerate(lineas, start = 1):
    if palabra.lower() in linea.lower():
        linea_numerada = f"{i:04d}: " + linea
        lineas_encontradas.append(linea_numerada)

for linea in lineas_encontradas:
    print(linea)
if guardar:
    with open(ruta_salida, "w", encoding = "utf-8") as fichero:
        fichero.writelines(lineas_encontradas)
        print("Búsqueda guardada en:", ruta_salida)
