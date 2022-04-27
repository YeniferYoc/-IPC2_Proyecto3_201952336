from Servicio import *
class Empresa:
    def __init__(self, nombre, servicios):
        self.nombre = nombre
        self.servicios = servicios
        
    def getNombre(self):
        return self.nombre
    
    def getServicios(self):
        return self.servicios

    def mostrar_empresa(self):
        print("NOMBRE:  "+str(self.nombre))
        for servicio in self.servicios: 
            servicio.mostrar_servicio()