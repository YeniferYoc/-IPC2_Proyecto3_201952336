from sqlite3 import Date
from tkinter import filedialog as fd
from xml.dom import minidom
from xml.dom.expatbuilder import parseString
from Respuesta import *
from jinja2 import FileSystemBytecodeCache
from lista_men import lista_men
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
    lista_respuestas = []
    respuesta_solicitud = ''
    
    def analisis_solicitud(self, texto):
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
                                            fecha_correcta = Date(int(tokens[i+4].lexema_valido), int(tokens[i+2].lexema_valido), int(tokens[i].lexema_valido))
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

    def Positivos_negativos(self, arreglo_mensajes):
        #arreglo_sol = self.arreglo_solicitudes
            arreglo_sol = self.arreglo_solicitudes
            sol = arreglo_sol[0]
            arreglo_devolver = [None, None,0,0,0]
        #for sol in arreglo_sol:
            diccionario_buenas = sol.positivos
            diccionario_malas = sol.negativos
            mensajes = arreglo_mensajes
            arreglo_emp = []
            cont_b = 0
            cont_m = 0
            cont_n = 0
            cant_buenas = int(mensajes[0].cant_buenas)
            cant_malas = int(mensajes[0].cant_malas)
            contador_positivos = 0
            contador_negativos = 0
            contador_neutro = 0
            if cant_buenas == cant_malas:
                print("mensaje neutro")
                cont_n = 1
                contador_neutro +=1
            elif cant_buenas < cant_malas:
                print("mensjae negativo")
                cont_m = 1
                contador_negativos +=1
            else:
                print("mensaje positivo")
                contador_positivos += 1
                cont_b = 1
            for e in range(len(mensajes[0].empresas)):
                servicios_empresa = []
                for ser in mensajes[0].empresas[e].servicios:
                    nuevo_servicio= Servicio(ser.nombre_ser, ser.alias, cont_b,cont_m, cont_n)
                    servicios_empresa.append(nuevo_servicio)
                nueva_emp = Empresa(mensajes[0].empresas[e].nombre,servicios_empresa,cont_b, cont_m, cont_n)
                arreglo_emp.append(nueva_emp)
           
                
            for i in range(1, len(mensajes)):
                        cont_b = 0
                        cont_m = 0
                        cont_n = 0
                        cant_buenas = int(mensajes[i].cant_buenas)
                        cant_malas = int(mensajes[i].cant_malas)
                        if cant_buenas == cant_malas:
                            print("mensaje neutro")
                            cont_n = 1
                            contador_neutro +=1
                        elif cant_buenas < cant_malas:
                            contador_negativos += 1
                            print("mensaje negativo")
                            cont_m = 1
                        else:
                            contador_positivos += 1
                            print("mesnaje positvo")
                            cont_b = 1
                        for j in range(len(mensajes[i].empresas)):
                            empresa_nom = str(mensajes[i].empresas[j].nombre.upper())
                            encontre_emp = False
                            for m in range(len(arreglo_emp)):
                                nom_emp_yaesta = str(arreglo_emp[m].nombre.upper())
                                if empresa_nom == nom_emp_yaesta:
                                        print("encontre empresa "+empresa_nom)
                                        encontre_emp= True
                                        arreglo_emp[m].buenos += cont_b
                                        arreglo_emp[m].malos += cont_m
                                        arreglo_emp[m].neutros += cont_n
                                        for b in range(len(mensajes[i].empresas[j].servicios)):
                                            encontre_serv = False
                                            nom_serv = str(mensajes[i].empresas[j].servicios[b].nombre_ser.upper())
                                            for t in range(len(arreglo_emp[m].servicios)):
                                                nom_serv_yaesta = arreglo_emp[m].servicios[t].nombre_ser.upper()
                                                if nom_serv == nom_serv_yaesta:
                                                    print("encontre serv "+nom_serv)
                                                    encontre_serv = True
                                                    arreglo_emp[m].servicios[t].buenos += cont_b
                                                    arreglo_emp[m].servicios[t].malos += cont_m
                                                    arreglo_emp[m].servicios[t].neutros += cont_n
                                            if encontre_serv == False:
                                                nom_s = mensajes[i].empresas[j].servicios[b].nombre_ser
                                                ali = mensajes[i].empresas[j].servicios[b].alias
                                                nuevo_servicioo = Servicio(nom_s, ali,cont_b, cont_m, cont_n)
                                                arreglo_emp[m].servicios.append(nuevo_servicioo)
                            if encontre_emp == False:
                                    servicios_empresa = []
                                    for ser in mensajes[i].empresas[j].servicios:
                                        nuevo_servicio= Servicio(ser.nombre_ser, ser.alias, cont_b,cont_m, cont_n)
                                        servicios_empresa.append(nuevo_servicio)
                                    nueva_emp = Empresa(mensajes[i].empresas[j].nombre,servicios_empresa,cont_b, cont_m, cont_n)
                                    arreglo_emp.append(nueva_emp)
                    
            solicitud_completa = Solicitud(sol.fecha, diccionario_buenas, diccionario_malas, arreglo_emp, mensajes)
            self.arreglo_respuesta.append(solicitud_completa)
            for emp in arreglo_emp:
                emp.mostrar_empresa()
            arreglo_devolver[0] = arreglo_emp
            arreglo_devolver[1] = mensajes
            arreglo_devolver[2] = contador_neutro
            arreglo_devolver[3] = contador_negativos
            arreglo_devolver[4] = contador_positivos
            return arreglo_devolver
            

    def Mensaje_prueba(self, mensaje):
                analizador_mensaje = Analizador_Lexico()
                arreglo_pal_neg = self.arreglo_solicitudes[0].negativos
                arreglo_pal_pos = self.arreglo_solicitudes[0].positivos
                arreglo_emp = self.arreglo_solicitudes[0].empresas
                mensaje_prueb = None
                
                    
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
                                            fecha_correcta = Date(int(tokens[i+4].lexema_valido), int(tokens[i+2].lexema_valido), int(tokens[i].lexema_valido))
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

                salida = self.generar_xml_mensaje_prueba(mensaje_prueb)
                
                return salida
                

                     
    def Buscar_por_fecha(self, fecha1, fecha2, empresa_):
        arreglo_devolver =[]
        devolver_filtro_emp = []
        arreglo_res = self.lista_respuestas
        fecha_comp1 = Date(fecha1.año, fecha1.mes, fecha1.dia)
        fecha_comp2 = Date(fecha2.año, fecha2.mes, fecha2.dia)


        if fecha1.dia != 0 and fecha2.dia == 0:#QUIERE DECIR QUE SE QUIERE SOLO UNA FECHA
            for respuesta in arreglo_res:
                if respuesta.fecha == fecha_comp1:
                    arreglo_devolver.append(respuesta)
        elif fecha1 != 0 and fecha2 != 0: #SE QUIERE UN RANGO DE FECHAS
            for respuesta in arreglo_res:
                if respuesta.fecha >= fecha_comp1 and respuesta.fecha <= fecha_comp2:
                    arreglo_devolver.append(respuesta)
        
        if empresa_ == 'Todas':
            respuesta = self.generar_xml(arreglo_devolver)
            return respuesta
        else: 
            for respuesta in arreglo_devolver: 
                for empresa in respuesta.empresas:
                    if empresa.nombre.upper() == empresa_.upper():
                        devolver_filtro_emp.append(respuesta)
            respuesta = self.generar_xml(devolver_filtro_emp)
            return respuesta
    
    def Buscar_por_una_fecha(self, fecha1, empresa_):
            arreglo_devolver =[]
            devolver_filtro_emp = []
            arreglo_res = self.lista_respuestas
            fecha_comp1 = Date(fecha1.año, fecha1.mes, fecha1.dia)


            for respuesta in arreglo_res:
                if respuesta.fecha == fecha_comp1:
                    arreglo_devolver.append(respuesta)
        
            if empresa_ == 'Todas':
                respuesta = self.generar_xml(arreglo_devolver)
                return respuesta
            else: 
                for respuesta in arreglo_devolver: 
                    for empresa in respuesta.empresas:
                        if empresa.nombre.upper() == empresa_.upper():
                            devolver_filtro_emp.append(respuesta)
                respuesta = self.generar_xml(devolver_filtro_emp)
                return respuesta
            



    def Generar_lista_respuestas(self):
        todos_mensajes = self.arreglo_solicitudes[0].mensajes
        
        lista_mensajes_a_ordenar = []
        lista_mensajes_a_ordenar.append(todos_mensajes[0])
        lista_mensajes_general = []
        lista = lista_men(todos_mensajes[0].fecha,lista_mensajes_a_ordenar)
        lista_mensajes_general.append(lista)
        for i in range(1,len(todos_mensajes)): 
            encontre_fecha = False
            for j in range(len(lista_mensajes_general)):
                if lista_mensajes_general[j].fecha == todos_mensajes[i].fecha:
                    encontre_fecha = True
                    lista_mensajes_general[j].mensajes.append(todos_mensajes[i])
            if encontre_fecha == False:
                nueva_lista = []
                nueva_lista.append(todos_mensajes[i])
                nueva_objeto = lista_men(todos_mensajes[i].fecha, nueva_lista)
                lista_mensajes_general.append(nueva_objeto)
        
        for imp in lista_mensajes_general:
            imp.dar_todo()
        for a in lista_mensajes_general:
            empresas_mensajes = self.Positivos_negativos(a.mensajes)
            empresas = empresas_mensajes[0]
            mensajes = empresas_mensajes[1]
            neutros = empresas_mensajes[2]
            positivos = empresas_mensajes[4]
            negativos = empresas_mensajes[3]
            total = neutros+positivos+negativos
            nueva_respuesta = Respuesta(a.fecha,total, positivos, negativos, neutros,empresas,mensajes )
            self.lista_respuestas.append(nueva_respuesta)
        for respuesta in self.lista_respuestas:
            respuesta.dar_todo()
        self.respuesta_solicitud = self.generar_xml(self.lista_respuestas)
        print(self.respuesta_solicitud)
        return self.respuesta_solicitud


    def generar_xml(self, lista_res):
        respuesta = '''
        <?xml version="1.0"?>\n
            <lista_respuestas>\n
        '''
        for respuesta_lista in lista_res:
            respuesta += '<respuesta>\n'
            respuesta+= '<fecha>'+str(respuesta_lista.fecha)+'</fecha>\n <mensajes>'
            respuesta += '<total>'+str(respuesta_lista.total)+'</total>\n <positivos>'+str(respuesta_lista.positivos)+'</positivos>\n'
            respuesta += '<negativos>'+str(respuesta_lista.negativos)+'</negativos>\n <neutros>'+str(respuesta_lista.neutros)+' </neutros></mensajes>\n <analisis>'
            for empresa in respuesta_lista.empresas:
                respuesta += '<empresa nombre=\"'+ str(empresa.nombre)+'\">\n <mensajes>'
                total_men_emp = int(empresa.buenos)+int(empresa.malos)+int(empresa.neutros)
                respuesta += '<total>'+str(total_men_emp)+'</total>\n <positivos>'+str(empresa.buenos)+'</positivos>'
                respuesta += '<negativos>'+str(empresa.malos)+'</negativos> \n  <neutros>'+str(empresa.neutros)+'</neutros>'
                respuesta += ' </mensajes>\n <servicios>\n '
                for servicio in empresa.servicios:
                    respuesta += '<servicio nombre=\"'+str(servicio.nombre_ser)+'\">\n <mensajes>'
                    total_men_ser = int(servicio.buenos)+int(servicio.malos)+int(servicio.neutros)
                    respuesta += '<total>'+str(total_men_ser)+'</total>\n <positivos>'+str(servicio.buenos)+'</positivos>'
                    respuesta += '<negativos>'+str(servicio.malos)+'</negativos> \n  <neutros>'+str(servicio.neutros)+'</neutros>'
                    respuesta += ' </mensajes>\n'
                    respuesta += '</servicio>'
                respuesta += '</servicios>'
                respuesta += '</empresa>'
            respuesta +='</analisis>'
            respuesta += '</respuesta>'
        respuesta += '</lista_respuestas>'
        return respuesta
    
    def generar_xml_mensaje_prueba(self, mensaje):
        respuesta = '''
        <?xml version="1.0"?>\n
            <respuesta>\n '
        '''
        respuesta += ' <fecha>'+str(mensaje.fecha)+'</fecha>\n'
        respuesta += '<red_social>'+str(mensaje.red)+'</red_social>\n'
        respuesta += '<usuario>'+str(mensaje.usuario)+'</usuario>'
        respuesta += '<empresas>'
        for empresa in mensaje.empresas:
            respuesta += '<empresa nombre=\"'+str(empresa.nombre)+'\">\n'
            for servicio in empresa.servicios:
                respuesta += '<servicio>'+str(servicio.nombre_ser)+'</servicio>\n'
            respuesta += '</empresa>\n'
        respuesta += '</empresas>\n'
        respuesta += '<palabras_positivas>'+str(mensaje.cant_buenas)+'</palabras_positivas>\n'
        respuesta += '<palabras_negativas>'+str(mensaje.cant_malas)+'</palabras_negativas>\n'
        total_palabras = int(mensaje.cant_buenas)+int(mensaje.cant_malas)
        porcentaje_buenas = ((int(mensaje.cant_buenas)*100)/total_palabras)
        porcentaje_malas = 100-porcentaje_buenas
        respuesta += '<sentimiento_positivo>'+ str(porcentaje_buenas)+'% </sentimiento_positivo>\n'
        respuesta += '<sentimiento_negativo>'+str(porcentaje_malas)+'% </sentimiento_negativo>\n'
        buenas = int(mensaje.cant_buenas)
        malas = int(mensaje.cant_malas)
        sentimiento = 'neutro'
        if buenas == malas:
            sentimiento = 'neutro'
        elif buenas < malas:
            sentimiento = 'negativo'
        else:
            sentimiento = 'positivo'
        respuesta += '<sentimiento_analizado>'+sentimiento+'</sentimiento_analizado> </respuesta>'
        return respuesta






                                      

                                       

                    

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2  TOP INFERIOR TEMPORADA <1999-2000> -n 3
    archi1=open('entrada.xml', "r", encoding="utf-8")
    contenido=archi1.read()
    archi1.close()

    app = Analisis(contenido)
    #app.Positivos_negativos()

    print("pureba")
    final = app.Generar_lista_respuestas()
    print(final)

    archi2=open('mensaje.xml', "r", encoding="utf-8")
    contenido=archi2.read()
    archi2.close()
    print("MENSAJE PRUEBA---------------------------------------")
    app.Mensaje_prueba(contenido)


if __name__ == "__main__":
    main()
