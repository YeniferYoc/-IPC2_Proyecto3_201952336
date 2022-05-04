from Servicio import *
class Empresa:
    def __init__(self, nombre, servicios, buenos, malos, neutros):
        self.nombre = nombre
        self.servicios = servicios
        self.buenos = buenos
        self.malos = malos
        self.neutros = neutros
        
    def getNombre(self):
        return self.nombre
    
    def getServicios(self):
        return self.servicios

    def mostrar_empresa(self):
        print("NOMBRE:  emp "+str(self.nombre)+" buenos "+str(self.buenos)+" malos "+str(self.malos)+" neutros "+str(self.neutros))
        for servicio in self.servicios: 
            servicio.mostrar_servicio()