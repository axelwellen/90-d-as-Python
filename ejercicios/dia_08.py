# Analizador de notas

# dada una lista de notas:
# mostrar la media, nota máxima, nota mínima, aprobados, suspendidos

notas = [4.5,7.2,8.0,3.9,6.5]

def calcular_notas(notas):
    aprobados = sum(1 for n in notas if n>=5)
    return {
            "media":round(sum(notas)/len(notas),2),
            "nota_max":max(notas),
            "nota_min":min(notas),
            "aprobados":aprobados,
            "suspendidos":len(notas)-aprobados,
            "notas_ordenadas":sorted(notas)
            }


if __name__ == "__main__":
    resultados = calcular_notas(notas)
    print(resultados)
