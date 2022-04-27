from Token import Token

class Analizador_Lexico():
    lexema = ''
    tokens= []
    buenas = 0
    malas= 0
    estado = 1
    fila = 1
    columna = 1
    generar = False
    arr_buenas = []
    arr_malas = []
    contador_buenas = 0
    contador_malas = 0

    def analisis(self,entrada, arr_buenas, arr_malas):
        self.estado = 1
        self.lexema = ''
        self.tokens = []
        self.error = True
        self.arr_buenas = arr_buenas
        self.arr_malas = arr_malas
        self.buenas = 0
        self.malas = 0
        tipos = Token("lexema", -1)
        print(entrada)

        entrada = entrada + '#'
        #print(entrada)
        actual = ''
        longitud = len(entrada)

        for i in range(longitud):
            actual = entrada[i]
            #print("["+actual+"]")
            #print(str(self.estado)+"estasdo")
            
            if self.estado == 1:
                #print("entro"+str(i))
                if actual.isalpha():
                    #print('letra')
                    #print(actual)
                    #print(actual)
                    self.estado = 4
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.estado = 3
                    self.lexema += actual
                    continue
                elif actual == ':':
                    self.lexema += actual
                    self.AgregarToken(tipos.DOS_PUNTOS)
                    continue
                elif actual == '/':
                    self.lexema += actual
                    self.AgregarToken(tipos.DIAGONAL)
                    continue
                elif actual == ',':
                    self.lexema += actual
                    self.AgregarToken(tipos.COMA)
                    continue
                elif actual == ' ':
                    self.estado = 1
                    #continue
                elif actual == '\n':
                    self.estado = 1
                    continue
                elif actual =='\r':
                    self.estado = 1
                    continue
                elif actual == '\t':
                    self.estado = 1
                    continue
                elif actual == '#' and i ==longitud - 1:
                    print('EL ANALIZADOR LEXICO HA TERMINADO')
                    continue
                else:
                    self.lexema += actual
                    self.AgregarToken(tipos.DESCONOCIDO)
                    
                    self.error = False
                    print("ERROR")
                    continue
                
            
            #MANEJRAR LETRAS
            elif self.estado == 4:
                #print("entro")
                #print(actual)
                if actual == ' ' or actual == '\t' or actual == '\n' or actual == ':' or actual == ',':
                    if self.RESERVADA():
                        
                        if actual == ',':
                            self.lexema += actual
                            self.AgregarToken(tipos.COMA)
                            #continue
                        elif actual == ':':
                            self.lexema += actual
                            self.AgregarToken(tipos.DOS_PUNTOS)
                        elif actual == ' ':
                            
                            self.estado = 1
                            #continue
                        elif actual == '\n':
                            
                            self.estado = 1
                            
                        elif actual =='\r':
                            self.estado = 1
                            
                        elif actual == '\t':
                            self.estado = 1
                            continue
                        #print(i)
                        continue
                    else:
                        '''if self.Buenas_malas(self.arr_buenas, self.arr_malas):
                            pass'''

                        self.AgregarToken(tipos.LETRAS)
                        if actual == ',':
                            self.lexema += actual
                            self.AgregarToken(tipos.COMA)
                            #continue
                        elif actual == ':':
                            self.lexema += actual
                            self.AgregarToken(tipos.DOS_PUNTOS)
                        elif actual == ' ':
                            
                            self.estado = 1
                            #continue
                        elif actual == '\n':
                            
                            self.estado = 1
                            
                        elif actual =='\r':
                            self.estado = 1
                            
                        elif actual == '\t':
                            self.estado = 1
                            continue
                        else:
                            self.lexema += actual
                            self.columna += 1
                            self.AgregarToken(tipos.DESCONOCIDO)
                        continue 
                    
                
                else:
                    self.estado = 4
                    self.lexema += actual
                    continue
                    
            
            #ESTADO PARA MANEJAR NUMEROS
            elif self.estado == 3:
                if actual.isdigit():
                    self.estado = 3   
                    self.lexema += actual
                    continue

                else:
                    self.AgregarToken(tipos.NUMERO)
                    if actual == ',':
                            self.lexema += actual
                            self.AgregarToken(tipos.COMA)
                            continue
                    elif actual == '/':
                            self.lexema += actual
                            self.columna += 1
                            self.AgregarToken(tipos.DIAGONAL)
                            continue
                    elif actual == '\n':
                            self.estado = 1
                            continue
                    elif actual == ' ':
                            self.estado = 1
                            continue
                    elif actual == '\t':
                            self.estado = 1
                            continue
                    else:
                        self.lexema += actual
                        self.AgregarToken(tipos.DESCONOCIDO)
                    continue 
                     
            #ESTADO DE CADENAS
            elif self.estado == 5:
                if actual != '"':
                    print(actual)
                    self.estado = 5
                    self.columna +=1
                    self.lexema += actual
                    continue
                elif actual == '"':
                     
                    self.AgregarToken(tipos.CADENA)
                    self.columna +=1
                    if actual == '\n':
                            self.fila += 1
                            self.estado = 1
                            self.columna += 1
                            continue
                    elif actual == ' ':
                            self.estado = 1
                            self.columna += 1
                            continue
                    elif actual == '\t':
                            self.estado = 1
                            self.columna += 5
                            continue
                    continue
            


    def AgregarToken(self,tipo):
        nuevo_token = Token(self.lexema, tipo)
        tipos = Token("lexema", -1)
        self.tokens.append(nuevo_token)
        self.lexema = ""
        self.estado = 1
        
    def RESERVADA(self):
        entrada = self.lexema.upper() #LENGUAJE CASE SENSITIVE 
        
        tipos = Token("lexema", -1)
        if entrada == 'LUGAR':
            self.AgregarToken(tipos.LUGAR)
            return True
        elif entrada == 'FECHA':
            self.AgregarToken(tipos.FECHA)
            return True
        elif entrada == 'USUARIO':
            self.AgregarToken(tipos.USUARIO)
            return True
        elif entrada == 'RED':
            self.AgregarToken(tipos.RED)
            return True
        elif entrada == 'SOCIAL':
            self.AgregarToken(tipos.SOCIAL)
            return True
        
        #return False

    def Buenas_malas(self, buenas, malas):
        entrada = self.lexema.upper() 
        si_es = False

        #palabras_reservadas = ["FORMULARIO","TIPO","VALOR","FONDO","NOMBRE", "VALORES", "EVENTO", "ENTRADA", "INFO"]
        print(entrada)
        for buena in buenas:
            print(buena)
            if entrada == buena.upper():
                self.buenas += 1
                si_es = True
        for mala in malas:       
            if entrada == mala.upper():
                self.malas += 1
                si_es = True
        print(si_es)
        
        return si_es


    def Imprimir(self):
        print("---------------------------------------------LISTA DE TOKENS ---------------------------------------------")
        #print("entro imprimir")
        tipos = Token("lexema", -1)
        contador = 0
        #print(len(self.tokens))
        for token in self.tokens:
            #print(contador)
            if token.tipo != tipos.DESCONOCIDO:
                #print(contador)
                print("LEXEMA: "+token.getLexema()," TIPO: ",token.getTipo())
                print("---------------------------------------------------------------------")
    
    def ImprimirErrores(self):
        print("--------------------------------------------- LISTA DE ERRORES ---------------------------------------------")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo == tipos.DESCONOCIDO:
                #self.tokens_errorres.append(x)
                print("LEXEMA: "+x.getLexema())
                print("---------------------------------------------------------------------")

#ultimo