#Gustavo Brandao Tavares

class Analisar_Palavra () :

    lista_sufixos = {'1a' : ['o', 'ei', 'ai'], 
               '2a' : ['os', 'es', 'ais'], 
               '3a' : ['a', 'e', 'i'], 
               '4a' : ['om', 'em', 'aem'], 
               '5a' : ['ons', 'est', 'aist'], 
               '6a' : ['am', 'im', 'aim']
    }

    def __init__(self,palavra) :
        self.palavra = palavra
        self.sufixo = self.definir_sufixo()
        self.verbo_original = self.definir_verbo_original()
        self.tempo_verbal   = self.definir_tempo_verbal()
        self.pessoa_verbal  = self.definir_pessoa_verbal()

    def __str__(self):
        if self.sufixo == 'Não é um tempo verbal' :
            return 'Não é um tempo verbal '
        else :
            return self.palavra + " - verbo " + self.verbo_original + "," + self.tempo_verbal + "," + self.pessoa_verbal+" pessoa "


    def definir_sufixo (self) :

        for sufixo in self.lista_sufixos.values() :
            for su in sufixo :

                if su == self.palavra[len(self.palavra)-3:len(self.palavra)] :
                    sufixo = su
                    return sufixo

                if su == self.palavra[len(self.palavra)-2:len(self.palavra)] :
                    sufixo = su
                    return sufixo
                    
                if su == self.palavra[len(self.palavra)-1:len(self.palavra)] :
                    sufixo = su
                    return sufixo

        sufixo = 'Não é um tempo verbal'
        return sufixo
                    
    def definir_verbo_original (self) :

        verbo_original = self.palavra.replace(self.sufixo,'en')
        return verbo_original

    def definir_tempo_verbal (self) :

        for posicao,sufixo in self.lista_sufixos.items():

            for su in sufixo :

                if su == self.sufixo :
        
                    p = sufixo.index(su)
                    if p == 0 :
                        tempo_verbal = 'Presente' 
                        return tempo_verbal
                    if p == 1 :
                        tempo_verbal = 'Pretérito'
                        return tempo_verbal
                    if p == 2 :
                        tempo_verbal = 'Futuro'
                        return tempo_verbal
                
        tempo_verbal = ' '

        return tempo_verbal

    def definir_pessoa_verbal (self) :
        for posicao,sufixo in self.lista_sufixos.items():
            for su in sufixo :
                if su == self.sufixo :
                    pessoa_verbal = posicao
                    return pessoa_verbal
                
        pessoa_verbal = ' '

        return pessoa_verbal