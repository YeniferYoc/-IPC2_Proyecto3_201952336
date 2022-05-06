from Empresa import *
from Fecha import *
class Solicitud:
    def __init__(self,fecha, positivos, negativos, empresas, mensajes):
        self.positivos = positivos
        self.negativos = negativos
        self.empresas = empresas
        self.mensajes = mensajes
        self.fecha = fecha
        
    def getPositivos(self):
        return self.positivos
    
    def getNegativos(self):
        return self.negativos 

    def mostrar_solicitud(self):
        print("----------------------------------- SOLICITUD --------------------------------------")
        #print(self.fecha.dar_todo())
        print("POSITIVOS")
        for pos in self.positivos:
            print(pos)
        print("NEGATIVOS")
        for neg in self.negativos:
            print(neg)
        print("EMPRESAS")
        for emp in self.empresas:
            emp.mostrar_empresa()
        print("MENSAJES")
        for men in self.mensajes:
            men.dar_todo()
        