from django.shortcuts import render, redirect
import requests
# Create your views here.

endpoint = 'http://localhost:4000{}'


def index(request):
    if request.method == 'GET':
        entrada = request.GET.get('entrada_', None)
        mensaje_prueba = request.GET.get('mensaje_p', None)
        consul = request.GET.get('consulta', None)
        context = {
            'salida': None,
            'consulta':None,
            
        }
        
        if entrada is not None:
            url = endpoint.format('/enviar')

            analizar_xml = requests.get(url, {
                'entrada': entrada,
            })

            context = {
                'salida': analizar_xml.text,
            }
        if mensaje_prueba is not None:
            url = endpoint.format('/mensaje_prueba')

            analizar_mensaje_prueba = requests.get(url, {
                'mensaje': mensaje_prueba,
            })

            context = {
                'consulta': analizar_mensaje_prueba.text,
            }
        

        

        return render(request, 'index.html', context)

    elif request.method == 'POST':
        entrada = request.GET.get('entrada_', '')
        
        url = endpoint.format('/enviar')

        analizar_xml = requests.get(url, {
            'entrada': entrada,
        })

        context = {
            'salida': analizar_xml.text,
        }

        return render(request, 'index.html', context)

def Peticiones(request):
    if request.method == 'GET':
        dia = request.GET.get('dia', 0)
        mes = request.GET.get('mes', 0)
        año = request.GET.get('año', 0)
        empresa_1 =request.GET.get('empresa', 'Todas')
        dia1 = request.GET.get('dia1', 0)
        mes1 = request.GET.get('mes1', 0)
        año1 = request.GET.get('año1', 0)
        dia2 = request.GET.get('dia2', 0)
        mes2 = request.GET.get('mes2', 0)
        año2 = request.GET.get('año2', 0)
        empresa = request.GET.get('empresa_2', 'Todas')
        url = endpoint.format('/mostrar_respuesta')
        Mostrar_respuesta_xml = requests.get(url, {
                   
                })
        context = {
            'consulta': Mostrar_respuesta_xml.text,
             'peticion_1': None,
            'peticion_':None,
            'dia': 0,
            'mes':0,
            'año':0,
            'dia1': 0,
            'mes1': 0,
            'año1':0,
            'dia2':0,
            'mes2':0,
            'año2':0,
                }
        
        if dia1 == 0:
            print("no lee dia1")
            print(dia1)
            
       
            if dia != 0:
                url = endpoint.format('/peticiones_fecha_una')
                peticiones_fecha_una = requests.get(url, {
                    'dia': dia,
                    'mes': mes,
                    'año': año,
                    'empresa' :empresa_1,
                })
                context = {
                    'peticion_1': peticiones_fecha_una.text,
                }
            else: 
                pass
        else: 
            print("sds")
            print(dia1)
            url = endpoint.format('/peticiones_fecha')
            peticiones_fecha = requests.get(url, {
                    'dia1': dia1,
                    'mes1': mes1,
                    'año1': año1,
                    'dia2': dia2,
                    'mes2': mes2,
                    'año2': año2,
                    'empresa' :empresa,
            })
            context = {
                'peticion_': peticiones_fecha.text,
            }

        return render(request, 'Peticiones.html', context)



