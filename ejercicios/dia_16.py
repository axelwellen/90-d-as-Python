# contador de extensiones
#
# dada una lista de archivos
# cuantos archivos hay de cada extensión

archivos = ["a.txt", "b.pdf", "c.txt", "foto.jpg", "datos.csv", "otro.pdf"]

dic_ext = {}

for archivo in archivos:
    extension = archivo.split(".")[-1] # nos guardamos solo la extensión
    dic_ext[extension] = dic_ext.get(extension,0) +1 # el get devuelve el valor si existe, o sino un 0. Y le suma 1

for clave, valor in dic_ext.items():
    print(clave,"->",valor)

