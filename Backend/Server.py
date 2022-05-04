from flask import Flask, json, request, jsonify
from flask_cors import CORS
from Analizar_xml import *



# Inicializar flask
app = Flask(__name__)
CORS(app)

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


# Ruta Raiz
@app.route('/', methods=["GET"])
def Raiz():
    return jsonify({ "mensaje": "Servidor Levantado"}), 200


# OPERACIONES ------------ CALCULADORA
@app.route('/enviar', methods=["POST"])
def operar():
    # Parametros que nos envia el frontend
    print("entro")
    texto = str(request.json["entrada"])
    print(texto)
    print("entro")

    resul = 'funciona'

    resultado = resul
    print(resultado)
    return jsonify({"resultado": resultado}), resultado

# LETRAS ------------------------- FRASES 
@app.route('/frase_', methods=["PUT"])
def frases_conteo():
    # Parametros que nos envia el frontend
    print("entro")
    frase = request.json["frase"]
    palabras = len(frase.split(" "))
    print(palabras)

    vocales = 0
    for letra in frase:
        if letra.lower() in "aeiou":
            vocales+=1

    consonantes = 0
    for letra in frase:
        if letra.lower() in "bcdfghjklmnñpqrstvwyz":
            consonantes+=1

    return jsonify({"palabras": palabras,"vocales": vocales,"consonantes": consonantes}), 200

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
