class Servicio:
    def __init__(self, nombre_ser, alias ):
        self.nombre_ser = nombre_ser
        self.alias = alias
        
    def getNombre_ser(self):
        return self.nombre_ser

    def mostrar_servicio(self):
        print("NOMBRE:  "+str(self.nombre_ser))
        for a in self.alias: 
            print(a)