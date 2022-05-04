class Servicio:
    def __init__(self, nombre_ser, alias, buenos, malos, neutros ):
        self.nombre_ser = nombre_ser
        self.alias = alias
        self.buenos= buenos
        self.malos = malos 
        self.neutros = neutros
        
    def getNombre_ser(self):
        return self.nombre_ser

    def mostrar_servicio(self):
        print("NOMBRE Servicio:  "+str(self.nombre_ser)+" buenos "+str(self.buenos)+" malos "+str(self.malos)+" neutros "+str(self.neutros))
        for a in self.alias: 
            print(a)