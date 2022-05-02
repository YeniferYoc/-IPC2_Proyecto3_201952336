from Fecha import *
from Empresa import *
class Mensaje():
    def __init__(self,fecha, mensaje, usuario, red, cant_buenas, cant_malas, empresas):
        self.fecha = fecha
        self.mensaje = mensaje
        self.usuario = usuario
        self.red = red
        self.cant_buenas = cant_buenas
        self.cant_malas = cant_malas
        self.empresas = empresas

    def dar_todo(self):
        print("Fecha: "+self.fecha.dar_todo()+" usuario "+str(self.usuario)+" red social "+str(self.red)+" buenas "+str(self.cant_buenas)+" malas "+str(self.cant_malas))
        for empresa in self.empresas:
            empresa.mostrar_empresa()
        print(self.mensaje)