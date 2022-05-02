class Token():
    lexema_valido = ''
    tipo = 0


    PALABRA_RESERVADA = 1
    NUMERO = 2
    DIAGONAL = 3
    COMA = 4
    DESCONOCIDO = 6
    LUGAR = 7
    FECHA = 8
    DOS_PUNTOS = 9
    USUARIO = 10
    RED = 11
    SOCIAL = 12
    LETRAS = 13

    def __init__(self,lexema,tipo):
        self.lexema_valido = lexema
        self.tipo = tipo

    def getLexema(self):
        return self.lexema_valido

#ultimo
    def getTipo(self):
        if self.tipo == self.PALABRA_RESERVADA:
            return 'PALABRA_RESERVADA'
        elif self.tipo == self.NUMERO:
            return 'NUMERO'
        elif self.tipo == self.DIAGONAL:
            return 'DIAGONAL'
        elif self.tipo == self.COMA:
            return 'COMA'
        elif self.tipo == self.NUMERO:
            return "NUMERO"
        elif self.tipo == self.LETRAS:
            return "LETRAS"
        elif self.tipo == self.DESCONOCIDO:
            return "DESCONOCIDO"
        elif self.tipo == self.USUARIO:
            return 'USUARIO'
        elif self.tipo == self.RED:
            return 'RED'
        elif self.tipo == self.SOCIAL:
            return "SOCIAL"
        elif self.tipo == self.LUGAR:
            return "LUGAR"
        elif self.tipo == self.FECHA:
            return 'FECHA'
        elif self.tipo == self.DOS_PUNTOS:
            return 'DOS PUNTOS'
        