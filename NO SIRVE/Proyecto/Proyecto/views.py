from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.template import loader

'''def home(request):
    template = loader.get_template("index.html")
    respuesta = requests.get('http://127.0.0.1:5000/estudiante')
    context = respuesta.json()
    return HttpResponse(template.render(context, request))
    #return render(request, "index.html")
from django.shortcuts import render
from django.http import HttpResponse
import requests'''

# Create your views here.
endpoint = 'http://127.0.0.1:4000/'
def home(request):
    context = {
        'mascotas': [],
        'title' : 'Home'
    }
    try:
        response = requests.get(endpoint + 'getmascotas')
        mascotas = response.json()
        context['mascotas'] = mascotas
    except:
        print('API no esta corriendo!!')
    return render(request, 'index.html', context=context)


def add(request):
    context = {
        'title' : 'Agregar Mascotas'
    }
    return render(request, 'add.html', context=context) 