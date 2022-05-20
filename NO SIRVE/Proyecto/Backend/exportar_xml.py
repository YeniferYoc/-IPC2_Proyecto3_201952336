mensaje ='<?xml version="1.0"?>'
nombre= 'mi_xml'
nombre = nombre + ".xml"
file = open(nombre, "w")
file.write(mensaje)
file.close()