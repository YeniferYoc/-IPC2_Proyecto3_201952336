from tkinter import filedialog as fd
from xml.dom import minidom
from xml.dom.expatbuilder import parseString
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
    arreglo_solicitudes = []
    arreglo_respuesta = []
    
    def __init__(self, texto):
            self.analizador = Analizador_Lexico()
            
            doc = parseString(texto)
            solicitudes = doc.getElementsByTagName("solicitud_clasificacion")
            self.arreglo_solicitudes = []
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
                        palabra = palabra.replace("\n", "")
                        palabra = palabra.replace("á", "a")
                        palabra = palabra.replace("é", "e")
                        palabra = palabra.replace("í", "i")
                        palabra = palabra.replace("ó", "o")
                        palabra = palabra.replace("ú", "u")
                        palabra = palabra.upper()
                        arreglo_pal_pos.append(palabra)
                
                sent_neg = solicitud.getElementsByTagName('sentimientos_negativos')
                for sent in sent_neg:
                    palabras = sent.getElementsByTagName('palabra')
                    for palabra in palabras:
                        palabra  = str(palabra.childNodes[0].data)
                        palabra = palabra.replace(" ", "")
                        palabra = palabra.replace("\n", "")
                        palabra = palabra.replace("á", "a")
                        palabra = palabra.replace("é", "e")
                        palabra = palabra.replace("í", "i")
                        palabra = palabra.replace("ó", "o")
                        palabra = palabra.replace("ú", "u")
                        palabra = palabra.upper()
                        arreglo_pal_neg.append(palabra)
                

                empresas = solicitud.getElementsByTagName('empresa')
                for empresa in empresas:
                    nombre_eml = empresa.getElementsByTagName('nombre')[0]
                    nombre_em = ''
                    nombre_em = str(nombre_eml.firstChild.data)
                    nombre_em = nombre_em.replace(" ","")
                    nombre_em = nombre_em.replace("\n", "")
                    nombre_em = nombre_em.replace("á", "a")
                    nombre_em = nombre_em.replace("é", "e")
                    nombre_em = nombre_em.replace("í", "i")
                    nombre_em = nombre_em.replace("ó", "o")
                    nombre_em = nombre_em.replace("ú", "u")

                    print(nombre_em+"dddd")
                    servicios = empresa.getElementsByTagName('servicio')
                    arr_servicios = []
                    for servicio in servicios:
                        arreglo_alias = []
                        nombre_ser = str(servicio.attributes['nombre'].value)
                        nombre_ser = nombre_ser.replace(" ", "")
                        nombre_ser = nombre_ser.replace("\n", "")
                        nombre_ser = nombre_ser.replace("á", "a")
                        nombre_ser = nombre_ser.replace("é", "e")
                        nombre_ser = nombre_ser.replace("í", "i")
                        nombre_ser = nombre_ser.replace("ó", "o")
                        nombre_ser = nombre_ser.replace("ú", "u")
                        
                        aliass = servicio.getElementsByTagName('alias')
                        for alia in aliass:
                            alias = str(alia.firstChild.data)
                            alias = alias.replace(" ", "")
                            alias = alias.replace("\n", "")
                            alias = alias.replace("á", "a")
                            alias = alias.replace("é", "e")
                            alias = alias.replace("í", "i")
                            alias = alias.replace("ó", "o")
                            alias = alias.replace("ú", "u")
                            
                            arreglo_alias.append(alias)
                        
                        nuevo_servicio = Servicio(nombre_ser, arreglo_alias, 0,0,0)
                        arr_servicios.append(nuevo_servicio)
                    nueva_emp = Empresa(nombre_em,arr_servicios,0,0,0)
                    arreglo_emp.append(nueva_emp)
                print("long arreglo emp "+str(len(arreglo_emp)))
                mensajes = solicitud.getElementsByTagName('mensaje')
                for mens in mensajes:
                    usuario = ''
                    red = ''
                    mensaje = str(mens.childNodes[0].data) 
                    mensaje = mensaje.replace("á", "a")
                    mensaje = mensaje.replace("é", "e")
                    mensaje = mensaje.replace("í", "i")
                    mensaje = mensaje.replace("ó", "o")
                    mensaje = mensaje.replace("ú", "u")
                    self.analizador.tokens = []
                    self.analizador.analisis(mensaje)
                    #self.analizador.Imprimir()
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
                            print("empresas en mensaje"+str(len(empresas_mensaje)))
                    arreglo_mens.append(Mensaje(fecha, mensaje, usuario, red,cont, contador_malas, empresas_mensaje))
                
                nueva_solicitud = Solicitud(fecha,arreglo_pal_pos, arreglo_pal_neg, arreglo_emp, arreglo_mens)
                self.arreglo_solicitudes.append(nueva_solicitud)

            for solici in self.arreglo_solicitudes:
                solici.mostrar_solicitud()
            #self.Positivos_negativos(self.arreglo_solicitudes)

    def Positivos_negativos(self):
        arreglo_sol = self.arreglo_solicitudes
        for sol in arreglo_sol:
            diccionario_buenas = sol.positivos
            diccionario_malas = sol.negativos
            mensajes = sol.mensajes
            arreglo_emp = []
            cont_b = 0
            cont_m = 0
            cont_n = 0
            cant_buenas = int(sol.mensajes[0].cant_buenas)
            cant_malas = int(sol.mensajes[0].cant_malas)
            if cant_buenas == cant_malas:
                print("mensaje neutro")
                cont_n = 1
            elif cant_buenas < cant_malas:
                print("mensjae negativo")
                cont_m = 1
            else:
                print("mensaje positivo")
                cont_b = 1
            for e in range(len(sol.mensajes[0].empresas)):
                servicios_empresa = []
                for ser in sol.mensajes[0].empresas[e].servicios:
                    nuevo_servicio= Servicio(ser.nombre_ser, ser.alias, cont_b,cont_m, cont_n)
                    servicios_empresa.append(nuevo_servicio)
                nueva_emp = Empresa(sol.mensajes[0].empresas[e].nombre,servicios_empresa,cont_b, cont_m, cont_n)
                arreglo_emp.append(nueva_emp)
           
                
            for i in range(1, len(sol.mensajes)):
                        cont_b = 0
                        cont_m = 0
                        cont_n = 0
                        cant_buenas = int(sol.mensajes[i].cant_buenas)
                        cant_malas = int(sol.mensajes[i].cant_malas)
                        if cant_buenas == cant_malas:
                            print("mensaje neutro")
                            cont_n = 1
                        elif cant_buenas < cant_malas:
                            print("mensaje negativo")
                            cont_m = 1
                        else:
                            print("mesnaje positvo")
                            cont_b = 1
                        for j in range(len(sol.mensajes[i].empresas)):
                            empresa_nom = str(sol.mensajes[i].empresas[j].nombre.upper())
                            encontre_emp = False
                            for m in range(len(arreglo_emp)):
                                nom_emp_yaesta = str(arreglo_emp[m].nombre.upper())
                                if empresa_nom == nom_emp_yaesta:
                                        print("encontre empresa "+empresa_nom)
                                        encontre_emp= True
                                        arreglo_emp[m].buenos += cont_b
                                        arreglo_emp[m].malos += cont_m
                                        arreglo_emp[m].neutros += cont_n
                                        for b in range(len(sol.mensajes[i].empresas[j].servicios)):
                                            encontre_serv = False
                                            nom_serv = str(sol.mensajes[i].empresas[j].servicios[b].nombre_ser.upper())
                                            for t in range(len(arreglo_emp[m].servicios)):
                                                nom_serv_yaesta = arreglo_emp[m].servicios[t].nombre_ser.upper()
                                                if nom_serv == nom_serv_yaesta:
                                                    print("encontre serv "+nom_serv)
                                                    encontre_serv = True
                                                    arreglo_emp[m].servicios[t].buenos += cont_b
                                                    arreglo_emp[m].servicios[t].malos += cont_m
                                                    arreglo_emp[m].servicios[t].neutros += cont_n
                                            if encontre_serv == False:
                                                nom_s = sol.mensajes[i].empresas[j].servicios[b].nombre_ser
                                                ali = sol.mensajes[i].empresas[j].servicios[b].alias
                                                nuevo_servicioo = Servicio(nom_s, ali,cont_b, cont_m, cont_n)
                                                arreglo_emp[m].servicios.append(nuevo_servicioo)
                            if encontre_emp == False:
                                    servicios_empresa = []
                                    for ser in sol.mensajes[i].empresas[j].servicios:
                                        nuevo_servicio= Servicio(ser.nombre_ser, ser.alias, cont_b,cont_m, cont_n)
                                        servicios_empresa.append(nuevo_servicio)
                                    nueva_emp = Empresa(sol.mensajes[i].empresas[j].nombre,servicios_empresa,cont_b, cont_m, cont_n)
                                    arreglo_emp.append(nueva_emp)
                    
            solicitud_completa = Solicitud(sol.fecha, diccionario_buenas, diccionario_malas, arreglo_emp, mensajes)
            self.arreglo_respuesta.append(solicitud_completa)
            for emp in arreglo_emp:
                emp.mostrar_empresa()

    def Mensaje_prueba(self, mensaje):
                analizador_mensaje = Analizador_Lexico()
                arreglo_pal_neg = self.arreglo_solicitudes[0].negativos
                arreglo_pal_pos = self.arreglo_solicitudes[0].positivos
                arreglo_emp = self.arreglo_solicitudes[0].empresas
                
                    
                doc = parseString(mensaje)
                mensajes = doc.getElementsByTagName("mensaje")  
                for mens in mensajes:
                    usuario = ''
                    red = ''
                    mensaje = str(mens.childNodes[0].data) 
                    mensaje = mensaje.replace("á", "a")
                    mensaje = mensaje.replace("é", "e")
                    mensaje = mensaje.replace("í", "i")
                    mensaje = mensaje.replace("ó", "o")
                    mensaje = mensaje.replace("ú", "u")
                    analizador_mensaje.tokens = []
                    analizador_mensaje.analisis(mensaje)
                    #self.analizador.Imprimir()
                    tokens = analizador_mensaje.tokens
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
                            print("empresas en mensaje"+str(len(empresas_mensaje)))
                    mensaje_prueb = Mensaje(fecha, mensaje, usuario, red,cont, contador_malas, empresas_mensaje)
                    mensaje_prueb.dar_todo()
                     



                                      

                                       

                    

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2  TOP INFERIOR TEMPORADA <1999-2000> -n 3
    archi1=open('entrada.xml', "r", encoding="utf-8")
    contenido=archi1.read()
    archi1.close()

    app = Analisis(contenido)
    app.Positivos_negativos()

    archi2=open('mensaje.xml', "r", encoding="utf-8")
    contenido=archi2.read()
    archi2.close()
    print("MENSAJE PRUEBA---------------------------------------")
    app.Mensaje_prueba(contenido)


if __name__ == "__main__":
    main()
