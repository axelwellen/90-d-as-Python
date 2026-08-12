"""
    Herencia simple

    Crear clase base: 
    class EventoLog

    Y las clases hijas: 
    LoginEvent
    ErrorEvent

    Cada una debe tener método mostrar()
    Extra: clasificar eventos desde líneas de texto
"""
from pathlib import Path

class EventoLog:
    
    def __init__(self, ip, evento):
        self.ip = ip
        self.evento = evento
    
    def __str__(self):
        return f"Evento: {self.evento}, IP: {self.ip}"
    
    def mostrar(self):
        print(self)

class LoginEvent(EventoLog):
    
    def __str__(self):
        return f"Login Event: {self.evento}, IP: {self.ip}"
    
class ErrorEvent(EventoLog):
    
    def __str__(self):
        return f"Error Event: {self.evento}, IP: {self.ip}"
    
if __name__ == "__main__":
    
    OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
    name = "auth.log"
    ruta = OUTPUT_DIR / name

    with open(ruta, "r", encoding = "utf-8") as fichero: 
        lineas = fichero.readlines()
    
    eventos = []

    for linea in lineas:
        vec_linea = linea.split("-")
        ip = vec_linea[0].strip()
        evento = vec_linea[1].strip()
        if evento == "login ok":
            eventos.append(LoginEvent(ip,evento))
        elif "failed" in evento or "denied" in evento or "invalid" in evento:
            eventos.append(ErrorEvent(ip,evento))
        else:
            eventos.append(EventoLog(ip,evento))

    for evento in eventos:
        evento.mostrar()

