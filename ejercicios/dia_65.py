""" 
    Clase Usuario

    Crear una clase Usuario con: 
    - nombre
    - aciertos
    - errores
    Métodos: 
    - registrar_acierto
    - registrar_error
    - mostrar_estadísticas
    Extra: Calcular el porcentaje de acierto
"""

class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.aciertos = 0
        self.errores = 0

    def registrar_acierto(self):
        self.aciertos += 1

    def registrar_error(self):
        self.errores += 1

    def mostrar_estadisticas(self): 
        print(f"El usuario {self.nombre} lleva {self.aciertos} aciertos y {self.errores} errores")
        print(f"El usuario tiene un {self.porcentaje_acierto()}% de aciertos")
        
    def porcentaje_acierto(self):
        total = self.aciertos + self.errores
        if total == 0:
            return 0

        return round((self.aciertos / total) * 100,2)

if __name__ == "__main__":
    usuario = Usuario("Axel")
    usuario.registrar_acierto()
    usuario.registrar_error()
    usuario.registrar_acierto()
    usuario.mostrar_estadisticas()
    porc_aciertos = usuario.porcentaje_acierto()
