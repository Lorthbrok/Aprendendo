import pandas as pd


class Individual () :
    
    lista_genotipos = ('AA', 'Ai', 'BB', 'Bi', 'AB', 'ii')

    #Contador de  instâncias
    numero_individuos = 0

    #Tabela com dados de todas as intâncias da classe
    tabela_geral = pd.DataFrame(columns=['NOME','GENOTIPO','TIPO_SANGUINEO','AGLUTINOGENEOS','AGLUTININAS'])

    copia = []

    def __init__ (self, genotipo, nome = '') :
        
        self.__genotipo = genotipo
        self.__validar_genotipo()
        if self.__genotipo == 'ii' :
            pass
        else :
            self.__genotipo.capitalize()

        self.__nome = nome
        if self.__nome == '' :
            self.__nome = self.__gerar_nome()
        else :
            pass
        
        self.__tipo_sanguineo = self.__definir_tipo_sanguineo()
        self.__aglutinogeneos = self.__definir_aglutinogeneos()
        self.__aglutininas = self.__definir_aglutininas()

        #Usando Pandas para criar uma tabela para exibir dados
        colunas = ['NOME','GENOTIPO','TIPO_SANGUINEO','AGLUTINOGENEOS','AGLUTININAS']
        dados = [[self.__nome, self.__genotipo, self.__tipo_sanguineo, self.__aglutinogeneos, self.__aglutininas]]
        self.__tabela= tabela = pd.DataFrame(data=dados,columns=colunas)

        Individual.tabela_geral.loc[Individual.numero_individuos] = [self.__nome, self.__genotipo, self.__tipo_sanguineo, self.__aglutinogeneos, self.__aglutininas]
        Individual.numero_individuos = Individual.numero_individuos + 1

    
    def __str__ (self) :
        
        print(self.__tabela)
        
        return ' '
    

    #Funcao para definir o tipo sanguineo
    def __definir_tipo_sanguineo (self) :

        if self.__genotipo == 'AA' :
            self.__tipo_sanguineo = 'A'

        if self.__genotipo == 'Ai' :
            self.__tipo_sanguineo = 'A'

        if self.__genotipo == 'BB' :
            self.__tipo_sanguineo = 'B'

        if self.__genotipo == 'Bi' :
            self.__tipo_sanguineo = 'B'

        if self.__genotipo == 'AB' :
            self.__tipo_sanguineo = 'AB'

        if self.__genotipo == 'ii' :
            self.__tipo_sanguineo = 'O'

        return self.__tipo_sanguineo

    #Funcao que gera o nome automaticamete quando nao for definido no construtor
    def __validar_genotipo (self) :

        if self.__genotipo not in Individual.lista_genotipos :

            raise 'Valor de genotipo inválido'                   
    

    #Funcao que validaçao do valor de entrada do genotipo
    def __gerar_nome (self) :

        num_ind = Individual.numero_individuos + 1             
        
        nome = 'Indiv-N' + str(num_ind)
        
        return nome

    #Funcao que definir os aglutinogeneos
    def __definir_aglutinogeneos (self) :

        if self.__tipo_sanguineo == 'A' :
            self.__aglutinogeneos = 'A'

        if self.__tipo_sanguineo == 'B' :
            self.__aglutinogeneos = 'B'

        if self.__tipo_sanguineo == 'AB' :
            self.__aglutinogeneos = 'AB'

        if self.__tipo_sanguineo == 'O' :
            self.__aglutinogeneos = 'Não possui'
        
        return self.__aglutinogeneos

    #Funcao que definir as aglutininas
    def __definir_aglutininas (self) :
        
        if self.__tipo_sanguineo == 'A' :
            self.__aglutininas = 'Anti-B'
        
        if self.__tipo_sanguineo == 'B' :
            self.__aglutininas = 'Anti-A'
        
        if self.__tipo_sanguineo == 'AB' :
            self.__aglutininas = 'Não possui'
        
        if self.__tipo_sanguineo == 'O' :
            self.__aglutininas = 'Anti-A e Anti-B'
        
        return self.__aglutininas

    #Funçoes para ler os atributos privados
    def ler_genotipo (self) :

        return print(self.__genotipo)

    def ler_tipo_sanguineo (self) :
        
        return print(self.__tipo_sanguineo)
    
    def ler_nome (self) :

        return print(self.__nome)
    
    def ler_aglutinogeneos (self) :
        
        if self.__aglutinogeneos == '' :
            return print('Náo possue aglutinogeneos')
        else :
            return print(f'Aglutinogeneos do tipo {self.__aglutinogeneos}')
    
    def ler_aglutininas (self) :

        if self.__aglutininas == '' :
            return print('Não possue aglutininas') 
        else :
            return print(f'Aglutotinas do tipo {self.__aglutininas}')

    #Funcao que analisa a possibilidade de doação de sangue
    def doar_sangue (self, quem_recebe) :
        
        if self.__tipo_sanguineo == 'A' and quem_recebe.__tipo_sanguineo == 'A' :
            return print(f'O/A{self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) PODE doar sangue para o/a {quem_recebe.__nome} TIPO_SANGUINEO({quem_recebe.__tipo_sanguineo})')

        elif  self.__tipo_sanguineo == 'A' and quem_recebe.__tipo_sanguineo == 'AB' :
            return print(f'O/A {self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) PODE doar sangue para o/a {quem_recebe.__nome} TIPO_SANGUINEO({quem_recebe.__tipo_sanguineo})')

        elif self.__tipo_sanguineo == 'B' and quem_recebe.__tipo_sanguineo == 'B' :
            return print(f'O/A{self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) PODE doar sangue para o/a {quem_recebe.__nome} TIPO_SANGUINEO({quem_recebe.__tipo_sanguineo})')

        elif self.__tipo_sanguineo == 'B' and quem_recebe.__tipo_sanguineo == 'AB' :
            return print(f'O/A {self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) PODE doar sangue para o/a {quem_recebe.__nome} TIPO_SANGUINEO({quem_recebe.__tipo_sanguineo})')

        elif self.__tipo_sanguineo == 'AB' and quem_recebe.__tipo_sanguineo == 'AB' :
            return print(f'O/A {self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) PODE doar sangue para o/a {quem_recebe.__nome} TIPO_SANGUINEO({quem_recebe.__tipo_sanguineo})')
        
        elif self.__tipo_sanguineo == 'O' :
            return print(f'O/A {self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) PODE doar sangue para o/a {quem_recebe.__nome} TIPO_SANGUINEO({quem_recebe.__tipo_sanguineo})')
        
        else :
            return print(f'O/A {self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) NÂO pode doar sangue para o/a {quem_recebe.__nome} TIPO_SANGUINEO({quem_recebe.__tipo_sanguineo})')
    
    #Funcao que analisa a possibilidade da recepçao de sangue
    def receber_sangue (self, quem_doa) :
        if self.__tipo_sanguineo == 'A' and quem_doa.__tipo_sanguineo == 'A' or 'O':
            return print(f'O/A {self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) PODE receber sangue do o/a {quem_doa.__nome} TIPO_SANGUINEO({quem_doa.__tipo_sanguineo})')
        
        elif self.__tipo_sanguineo == 'B' and quem_doa.__tipo_sanguineo == 'B' or 'O':
            return print(f'O/A {self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) PODE receber sangue do o/a {quem_doa.__nome} TIPO_SANGUINEO({quem_doa.__tipo_sanguineo})')
        
        elif self.__tipo_sanguineo == 'AB' and quem_doa.__tipo_sanguineo == 'A' or 'O' or 'B' or 'AB' :
            return print(f'O/A {self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) PODE receber sangue do o/a {quem_doa.__nome} TIPO_SANGUINEO({quem_doa.__tipo_sanguineo})')
        
        elif self.__tipo_sanguineo == 'O' and quem_doa.__tipo_sanguineo == 'O':
            return print(f'O/A {self.__nome}  TIPO_SANGUINEO({self.__tipo_sanguineo}) PODE receber sangue do o/a {quem_doa.__nome} TIPO_SANGUINEO({quem_doa.__tipo_sanguineo})')
        
        else:
            return print(f'O/A {self.__nome} TIPO_SANGUINEO({self.__tipo_sanguineo}) NÂO pode receber sangue do o/a {quem_doa.__nome} TIPO_SANGUINEO({quem_doa.__tipo_sanguineo})')

    #Funcao que analisa as possiveis combinaçoes de genotipos entre dois objetos
    def combinar_genotipo (self, outro_individuo, gambiarra=True) :
        
        g1 = []
        g2 = []
        combinacao = []
        gambiarra = gambiarra

        for string in self.__genotipo :
            g1.append(string)
        
        for string in outro_individuo.__genotipo :
            g2.append(string)
        
        for s1 in g1 :
            for s2 in g2 :
                unir_string = s1 + s2
                if unir_string in combinacao :
                    pass
                else :
                    combinacao.append(unir_string)

        for c in combinacao :
            if c[0] == 'i' and c[1] != 'i' :
                reagrupar_string = c[::-1]
                combinacao.remove(c)
                combinacao.append(reagrupar_string)
                Individual.copia = combinacao.copy()
            else:
                Individual.copia = combinacao.copy()

        if gambiarra == True :
            return print(f'Os possíveis genótipos resultantes do cruzamento entre {self.__nome} e {outro_individuo.__nome} são {combinacao}')
        else :
            pass

    #Funcao que analisa as possiveis combinações de tipos sanguineos entre dois objetos
    def combinar_sangue (self, outro_individuo) :
        
        self.combinar_genotipo(outro_individuo, gambiarra=False)

        lista_sangue = []

        for genotipo in Individual.copia :
                
                if genotipo == 'AA' :
                    lista_sangue.append('A')
                if genotipo == 'Ai' :
                    lista_sangue.append('A')
                if genotipo == 'BB' :
                    lista_sangue.append('B')
                if genotipo == 'Bi' :
                    lista_sangue.append('B')
                if genotipo == 'AB' :
                    lista_sangue.append('AB')
                if genotipo == 'ii' :
                    lista_sangue.append('ii')

        def remover_repetidos (lista_sangue = lista_sangue) :
            remover = set(lista_sangue)
            lista_sangue = list(remover)

        return print(f'Os possíveis tipos sanguíneos resultantes do cruzamento entre o {self.__nome} e {outro_individuo.__nome} é {lista_sangue}')