"""
    Clase Palabra

    crear una clase palabra
    añadir el método mostrar
    Extra: añadir el método es_de_nivel(nivel)
"""

class Palabra: 
    def __init__(self, de, es, nivel, tema):
        self.de = de
        self.es = es
        self.nivel = nivel.upper()
        self.tema = tema.lower()
        print(f"Se ha creado la palabra {self.de}")

    def __str__(self):
        return f"{self.de} -> {self.es} [{self.nivel}/{self.tema}]"
    
    def mostrar(self):
        print(self)

    def cambiar_nivel(self,nivel):
        nivel_antiguo = self.nivel
        self.nivel = nivel
        print(f"Modificado el nivel de {nivel_antiguo} a {self.nivel}")
    
    def es_de_nivel(self, nivel):
        return self.nivel == nivel.upper().strip()

if __name__ == "__main__":
    palabra = Palabra("hallo","hola","B1","alltag")

    palabra.mostrar()
    print("La palabra es de nivel A1:",palabra.es_de_nivel("A1"))
    
    palabra.cambiar_nivel("A1")
    
    palabra.mostrar()
    print("La palabra es de nivel A1:",palabra.es_de_nivel("A1"))
