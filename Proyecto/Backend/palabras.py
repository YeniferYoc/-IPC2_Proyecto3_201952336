from sqlite3 import Date


arreglo_pal_pos = ['buenom mi', 'excelente','jj']
mensaje = str('Lugar y fecha: Guatemala, 01/04/2022 15:01 Usuario: map0001@usac.edu Red social: Twitter El servicio en la USAC para inscripción fue muy buen mi bueno mi o y me siento muy satisfecho.') 

cont = 0
for pal in arreglo_pal_pos:
    print(pal)
    if pal in mensaje:
        print("si")
for pal in arreglo_pal_pos:
    if pal in mensaje:
        cont +=1
print(cont)
'''palabras = ['bueno', 'malo']
cadena = 'hola bueno yo bueno'

for pal in palabras:
    if pal in cadena:
        print("si")
if 'bueno' in  palabras:
    print("yo")'''

fecha1 = '1/2/2022'
fecha2 = '2/1/2022'

nueva = Date(2022,2,1)
nueva2 = Date(2022,2,1)
if nueva < nueva2:
    print("saber que hizo")
elif nueva == nueva2:
    print("ifua")
else:
    print("pueda que funcione ")

salida = 'a'
for i in range(10):
    salida += 'a'
print(salida)