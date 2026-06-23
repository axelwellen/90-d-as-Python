# eliminador de duplicados
# dada una lista con elementos repetidos: 
# - mostrar lista original
# - mostrar lista sin duplicados
# - mostrar número de duplicados eliminados
# Extra: conservar el orden original

usuarios = ["ana", "pepe", "ana", "luis", "pepe", "marta", "ana"]

def eliminar_duplicados(usuarios):
    lista_sin_duplicados = []
    for usuario in usuarios:
        if usuario not in lista_sin_duplicados:
            lista_sin_duplicados.append(usuario)
    duplicados_eliminados = len(usuarios)-len(lista_sin_duplicados)
    return{
            "lista_original":usuarios,
            "lista_sin_duplicados":lista_sin_duplicados,
            "duplicados_eliminados":duplicados_eliminados
            }


if __name__ == "__main__":
    print(eliminar_duplicados(usuarios))
