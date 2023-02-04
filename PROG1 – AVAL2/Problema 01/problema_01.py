#Gustavo Brandao Tavares

class Check_Sequencia () :

    copiar = []

    def __init__ (self, N, sequencia) :
        self.N = N
        self.sequencia = list(sequencia)
        self.segmentos = []

    
        self.dividir_segmentos()
        self.valor_M_Alternada = self.definir_valor()
        
        self.validando = self.validar()

        if self.validando == False :
            self.valor_M_Alternada = 'NAO'

    def dividir_segmentos(self) :

        for n in self.sequencia:   

            if n < 0 :
                self.valor_M_Alternada = 'NAO'
                self.segmentos.clear()
                break

            self.copiar.append(n)

            if len(self.segmentos) == 0 :
                self.segmentos.append(self.copiar[0:len(self.copiar)])
                self.copiar.clear()
            
            if len(self.copiar) > len(self.segmentos[-1]) :
                self.segmentos.append(self.copiar[0:len(self.copiar)])
                self.copiar.clear()

                
    def verificar_par_impar(self):

        if len(self.segmentos) == 0 :
            return 'NAO'

        even = True

        for sublista in self.segmentos:
            for numero in sublista:
                if even:
                    if numero % 2 == 0:
                        continue
                    else:
                        return 'False'
                else:
                    if numero % 2 == 1:
                        continue
                    else:
                        return False
                    
            even = not even

        return True
    
    def definir_valor (self):

        if self.verificar_par_impar() == True :
            return len(self.segmentos)
        else :
            return 'NAO'
    
    def __str__ (self) :

        return str(self.valor_M_Alternada) + "\n%"
    
    def validar (self) :
        contador = 0

        if self.N != len(self.sequencia) :
            return False
        
        for sublista in self.segmentos :
            for num in sublista :
                contador = contador + 1
            
        if contador < len(self.sequencia) :
            return False

