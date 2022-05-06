from Empresa import *
from Fecha import *
class Respuesta:
    def __init__(self,fecha,total, positivos, negativos,neutros, empresas, mensajes):
        self.positivos = positivos
        self.negativos = negativos
        self.empresas = empresas
        self.mensajes = mensajes
        self.fecha = fecha
        self.neutros = neutros
        self.total = total
        
    def getPositivos(self):
        return self.positivos
    
    def getNegativos(self):
        return self.negativos 

    def dar_todo(self):
        print("----------------------------------- RESPUESTA --------------------------------------")
        #print(self.fecha.dar_todo())
        print("FECHA: "+str(self.fecha)+" TOTAL DE MENSAJES EN ESTA FECHA: "+str(self.total))
        print("TOTAL DE MENSAJES POSITIVOS "+str(self.positivos)+" TOTAL DE MENSAJES NEGATIVOS "+str(self.negativos))
        print("TOTAL DE MESNAJES NEUTROS: "+str(self.neutros))
        print("EMPRESAS")
        for emp in self.empresas:
            emp.mostrar_empresa()
        print("MENSAJES")
        for men in self.mensajes:
            men.dar_todo()
        