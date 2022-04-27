from tkinter import filedialog as fd
from xml.dom import minidom

from pyparsing import Regex
from Empresa import Empresa
from Servicio import Servicio
from Solicitud import Solicitud
from Analizador_Lexico import *
import re 
class Analisis():
    
    def __init__(self):
            self.analizador = Analizador_Lexico()
            print("AQUI SE SELECCIONAN LOS DATOS ")
            print("")
            nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
            
            doc = minidom.parse(nombrearch)
            solicitudes = doc.getElementsByTagName("solicitud_clasificacion")
            arreglo_solicitudes = []
            for solicitud in solicitudes:
                arreglo_pal_pos =[]
                arreglo_pal_neg = []
                arreglo_emp = []
                arreglo_mens = []
                

                sent_posi = solicitud.getElementsByTagName('sentimientos_positivos')
                for sent in sent_posi:
                    palabras = sent.getElementsByTagName('palabra')
                    for palabra in palabras:
                        palabra  = str(palabra.childNodes[0].data)
                        palabra = palabra.replace(" ", "")
                        palabra = palabra.upper()
                        arreglo_pal_pos.append(palabra)
                
                sent_neg = solicitud.getElementsByTagName('sentimientos_negativos')
                for sent in sent_neg:
                    palabras = sent.getElementsByTagName('palabra')
                    for palabra in palabras:
                        palabra  = str(palabra.childNodes[0].data)
                        palabra = palabra.replace(" ", "")
                        palabra = palabra.upper()
                        arreglo_pal_neg.append(palabra)
                
                mensajes = solicitud.getElementsByTagName('mensaje')
                for mens in mensajes:
                    mensaje = str(mens.childNodes[0].data) 
                    self.analizador.tokens = []
                    self.analizador.contador_buenas = 0
                    self.analizador.contador_malas = 0
                    self.analizador.analisis(mensaje, arreglo_pal_pos, arreglo_pal_neg)
                    self.analizador.Imprimir()
                    cont = 0
                    contador_malas = 0
                    prov = mensaje.upper()
                    for pal in arreglo_pal_neg:
                        if pal in prov:
                            contador_malas +=1
                    for pal in arreglo_pal_pos:
                        if pal in prov:
                            cont +=1
                    print(contador_malas)
                    print(cont)

                    arreglo_mens.append(mensaje)
                
                empresas = solicitud.getElementsByTagName('empresa')
                for empresa in empresas:
                    nombre_em = empresa.childNodes[0].data
                    servicios = empresa.getElementsByTagName('servicio')
                    arr_servicios = []
                    for servicio in servicios:
                        arreglo_alias = []
                        nombre_ser = servicio.attributes['nombre'].value
                        aliass = servicio.getElementsByTagName('alias')
                        for alia in aliass:
                            alias = str(alia.firstChild.data)
                            print(alias)
                            arreglo_alias.append(alias)
                        
                        nuevo_servicio = Servicio(nombre_ser, arreglo_alias)
                        arr_servicios.append(nuevo_servicio)
                    nueva_emp = Empresa(nombre_em,arr_servicios)
                    arreglo_emp.append(nueva_emp)
                
                nueva_solicitud = Solicitud(arreglo_pal_pos, arreglo_pal_neg, arreglo_emp, arreglo_mens)
                arreglo_solicitudes.append(nueva_solicitud)

            for solici in arreglo_solicitudes:
                solici.mostrar_solicitud()
                        

                    

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2  TOP INFERIOR TEMPORADA <1999-2000> -n 3

   app = Analisis()

if __name__ == "__main__":
    main()
