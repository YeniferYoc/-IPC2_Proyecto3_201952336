arreglo_pal_pos = ['bueno', 'excelente','satisfecho']
mensaje = str('Lugar y fecha: Guatemala, 01/04/2022 15:01 Usuario: map0001@usac.edu Red social: Twitter El servicio en la USAC para inscripción fue muy bueno y me siento muy satisfecho.') 

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