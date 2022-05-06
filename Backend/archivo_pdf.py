from reportlab.pdfgen import canvas

cadena= 'hola\n'
cadena+= 'como\n'
cadena += 'estas\n'
c = canvas.Canvas("hola-mundo.pdf")
c.drawString(100,750,'cadenad')
c.drawString(100,780,'cadena')
c.drawString(100,810,'cadena')
c.drawString(100,850,'cadena')
c.save()