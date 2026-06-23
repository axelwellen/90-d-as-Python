# Limpiador de nombres de archivo
# Tenemos la lista archivos, y tenemos que limpiar los nombres: quitar espacios al inicio y al final, pasar todo a minúscula, cambiar espacios por _

archivos = ["informe final .pdf", "foto vacaciones.JPG", "datos_enero.csv", "backup final .zip "]

def limpiador_nombres_archivo(archivos):
    for indice, archivo in enumerate(archivos):
        aux = archivo.lower().split(".")
        archivos[indice] = aux[0].strip().replace(" ","_") + "." + aux[1].strip() # borra espacios del inicio y del final, pasa a minusulas, sustituye " " por "_"
    return archivos
if __name__ == "__main__":
    archivos_limpios = limpiador_nombres_archivo(archivos)
    print(archivos_limpios)

