# comparador de listas
# tenemos dos listas de alumnos
# mostrar:
# - Alumnos en ambos grupos
# - solo en A
# - solo en B
# - todos los alumnos sin repetir

grupo_a = ["ana", "pepe", "luis", "marta"]
grupo_b = ["luis", "marta", "carlos", "elena"]

def comparar_grupos(ga, gb):
    set_a = set(ga)
    set_b = set(gb)
    return {
            "ambos_grupos":set_a.intersection(set_b),
            "grupo_a":set_a.difference(set_b),
            "grupo_b":set_b.difference(set_a),
            "todos": set_a.union(set_b)
            }

if __name__ == "__main__":
    print(comparar_grupos(grupo_a, grupo_b))
