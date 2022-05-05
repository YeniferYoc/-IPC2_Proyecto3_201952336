from Mensaje import *
class lista_men():
    def __init__(self,fecha,mensajes):
        self.mensajes = mensajes
        self.fecha = fecha

    def dar_todo(self):
        print(str(self.fecha))
        for mensaje in self.mensajes:
            mensaje.dar_todo()