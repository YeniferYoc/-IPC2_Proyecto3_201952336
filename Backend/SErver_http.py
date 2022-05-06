from flask import Flask, Response,json, request, jsonify
from flask_cors import CORS
from Analizar_xml import *
from Fecha import *



# Inicializar flask
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})

# Métodos de peticiones

# GET -> recuperar informacion
# POST -> enviar informacion
# DELETE -> eliminar informacion
# PUT -> insertar informacion

# Códigos de HTTP

# 200 -> ok
# 201 -> objeto creado
# 400 -> peticion incorrecta
# 404 -> no se encontro
analisis_ = Analisis()

# Ruta Raiz
@app.route('/', methods=["GET"])
def Raiz():
    return jsonify({ "mensaje": "Servidor Levantado"}), 200


# OPERACIONES ------------ XML DE CARGAR
@app.route('/enviar', methods=["GET"])
def analizar_xml():
    # Parametros que nos envia el frontend
    print("entro")
    texto = str(request.args.get('entrada'))
    print(texto)
    if texto == "None":  
        print("none")
        resul = 'no jalo el texto'
    else:  
        print("ahdkf") 
        analisis_.analisis_solicitud(texto)
        resul = analisis_.Generar_lista_respuestas()
    
    print("entro")

    resultado = resul
    print(resultado)
    #Response(response = resultado)
    return str(resultado)

# OPERACIONES ------------ XML DE MENSAJE PRUEBA
@app.route('/mensaje_prueba', methods=["GET"])
def analizar_mensaje_prueba():
    # Parametros que nos envia el frontend
    print("entro")
    mensaje = str(request.args.get('mensaje'))
    print(mensaje)
    resul = analisis_.Mensaje_prueba(mensaje)
    
    print("entro")

    resultado = resul
    print(resultado)
    return str(resultado)

# OPERACIONES ------------ PETICIONESDE FECHA
@app.route('/peticiones_fecha', methods=["GET"])
def peticiones_fecha():
    # Parametros que nos envia el frontend
    print("entro")
    dia1 = int(request.args.get('dia1'))
    mes1 = int(request.args.get('mes1'))
    año1= int(request.args.get('año1'))
    dia2 = int(request.args.get('dia2'))
    mes2 = int(request.args.get('mes2'))
    año2 = int(request.args.get('año2'))
    empresa = str(request.args.get('empresa'))
    fecha1 = Fecha(dia1, mes1, año1)
    fecha2 = Fecha(dia2, mes2, año2)
    resul = analisis_.Buscar_por_fecha(fecha1, fecha2, empresa)
    
    print("entro")

    resultado = resul
    print(resultado)
    return str(resultado)

# OPERACIONES ------------ PETICIONESDE FECHA
@app.route('/peticiones_fecha_una', methods=["GET"])
def peticiones_fecha_una():
    # Parametros que nos envia el frontend
    print("entrodd")
    dia1 = int(request.args.get('dia'))
    mes1 = int(request.args.get('mes'))
    año1= int(request.args.get('año'))
    empresa = str(request.args.get('empresa'))
    fecha1 = Fecha(dia1, mes1, año1)
    print("ddd"+fecha1.dar_todo())
    print(año1)
    resul = analisis_.Buscar_por_una_fecha(fecha1, empresa)
    
    print("entro")

    resultado = resul
    print(resultado)
    return str(resultado)

# LETRAS ------------------------- MSTRAR LISTA DE RESPUESTAS
@app.route('/mostrar_respuesta', methods=["GET"])
def Mostrar_respuesta_xml():
    # Parametros que nos envia el frontend
    print("entro")
    resultado = analisis_.respuesta_solicitud

    return jsonify({"resultado": resultado}), 200

# NUMEROS PRIMOS --------------------------------------
@app.route('/primos', methods=["POST"])
def numeros_primos():
    numerop1 = int(request.json["inferior"])
    numerop2 = int(request.json["superior"])

    contador_primos = 0
    si_primo = False
    for i in range(numerop1, numerop2):
        divisor = 2
        print(i)
        if i < 2:
            si_primo = False
        if i % divisor != 0:
                    si_primo = True
                    contador_primos += 1           #Que va a determinar si es primo o no              
 
    print ("Hay", contador_primos, "numeros primos") #Total de numeros primos

    resultado = contador_primos
    return jsonify({"primos": resultado}), 200


if __name__ == '__main__':
    app.run(debug=True, port=4000)
