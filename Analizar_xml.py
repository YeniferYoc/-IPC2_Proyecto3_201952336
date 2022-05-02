from tkinter import filedialog as fd
from xml.dom import minidom
from Mensaje import Mensaje
from pyparsing import Regex
from Empresa import Empresa
from Fecha import Fecha
from Servicio import Servicio
from Solicitud import Solicitud
from Analizador_Lexico import *
import re 
from Token import Token
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
                fecha = Fecha(0,0,0)
                

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
                

                empresas = solicitud.getElementsByTagName('empresa')
                for empresa in empresas:
                    nombre_eml = empresa.getElementsByTagName('empresa')
                    nombre_em = ''
                    for nom in nombre_eml:

                        nombre_em = str(nom.firstChild.data)

                    print(nombre_em+"dddd")
                    servicios = empresa.getElementsByTagName('servicio')
                    arr_servicios = []
                    for servicio in servicios:
                        arreglo_alias = []
                        nombre_ser = servicio.attributes['nombre'].value
                        aliass = servicio.getElementsByTagName('alias')
                        for alia in aliass:
                            alias = str(alia.firstChild.data)
                            
                            arreglo_alias.append(alias)
                        
                        nuevo_servicio = Servicio(nombre_ser, arreglo_alias, 0,0,0)
                        arr_servicios.append(nuevo_servicio)
                    nueva_emp = Empresa(nombre_em,arr_servicios,0,0,0)
                    arreglo_emp.append(nueva_emp)
                
                mensajes = solicitud.getElementsByTagName('mensaje')
                for mens in mensajes:
                    usuario = ''
                    red = ''
                    mensaje = str(mens.childNodes[0].data) 
                    self.analizador.tokens = []
                    self.analizador.analisis(mensaje, arreglo_pal_pos, arreglo_pal_neg)
                    self.analizador.Imprimir()
                    tokens = self.analizador.tokens
                    print(len(tokens))
                    tipos = Token("lexema", -1)
                    
                    for i in range(len(tokens)):
                        if tokens[i].tipo == tipos.NUMERO:
                            
                            if tokens[i+1].tipo == tipos.DIAGONAL:
                                if tokens[i+2].tipo == tipos.NUMERO:
                                    if tokens[i+3].tipo == tipos.DIAGONAL:
                                        if tokens[i+4].tipo == tipos.NUMERO:
                                            fecha_correcta = Fecha(int(tokens[i].lexema_valido), int(tokens[i+2].lexema_valido), int(tokens[i+4].lexema_valido))
                                            fecha = fecha_correcta

                        
                        if tokens[i].tipo == tipos.USUARIO:
                            if tokens[i+1].tipo == tipos.DOS_PUNTOS:
                                if tokens[i+2].tipo == tipos.LETRAS:
                                    usuario = str(tokens[i+2].lexema_valido)
                                    
                        if tokens[i].tipo == tipos.RED:
                            if tokens[i+1].tipo == tipos.SOCIAL:
                                if tokens[i+2].tipo == tipos.DOS_PUNTOS:
                                    if tokens[i+3].tipo == tipos.LETRAS:
                                        red = str(tokens[i+3].lexema_valido)
                                        
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

                    empresas_mensaje = []
                    for emp in arreglo_emp:
                        if emp.nombre.upper() in prov:
                            servicios_con_mensaje = []
                            for servicio in emp.servicios:
                                if servicio.nombre_ser.upper() in prov:
                                    servicio_mens = servicio.nombre_ser
                                    servicio_nuevo = Servicio(servicio_mens, '', cont, contador_malas, 0)
                                    servicios_con_mensaje.append(servicio_nuevo)
                                for aliaas in servicio.alias:
                                    if aliaas.upper() in prov:
                                        alias_nom = servicio.nombre_ser
                                        servicio_nuevo = Servicio(alias_nom, '', cont, contador_malas, 0)
                                    servicios_con_mensaje.append(servicio_nuevo)
                                empresas_mensaje.append(Empresa(emp.nombre, servicios_con_mensaje, cont, contador_malas,0))

                    arreglo_mens.append(Mensaje(fecha, mensaje, usuario, red,cont, contador_malas, empresas_mensaje))
                
                nueva_solicitud = Solicitud(fecha,arreglo_pal_pos, arreglo_pal_neg, arreglo_emp, arreglo_mens)
                arreglo_solicitudes.append(nueva_solicitud)

            for solici in arreglo_solicitudes:
                solici.mostrar_solicitud()
                        

                    

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2  TOP INFERIOR TEMPORADA <1999-2000> -n 3

   app = Analisis()

if __name__ == "__main__":
    main()
