import math

class Vetor () :

    def __init__(self, *args) :

        if len(args) == 1 and isinstance(args[0], Vetor):
            self.__abcissa  = args[0].__abcissa
            self.__ordenada = args[0].__ordenada
        elif len(args) == 2 and all(isinstance(arg, (int, float)) for arg in args):
            self.__abcissa = args[0]
            self.__ordenada = args[1]
        else:
            raise TypeError("A instância deve ser criada a partir de outro vetor ou de dois números")
        
        self.__modulo   = self.calcularModulo()

    def __str__(self) :
        return f'<{self.__abcissa},{self.__ordenada}>'
    
    def calcularModulo(self) :
        modulo = math.sqrt(((self.__abcissa) ** 2) + ((self.__ordenada) ** 2))
        return modulo
    
    def __add__(self, vetor) :

        if not isinstance(vetor, Vetor):
            raise TypeError("A soma só pode ser realizada com outro vetor")
        
        somaAbcissa  = (self.__abcissa) + (vetor.__abcissa)
        somaOrdenada = (self.__ordenada) + (vetor.__ordenada)
        resultado = f'<{somaAbcissa},{somaOrdenada}>'
        return resultado
    
    def __sub__(self, vetor) :

        if not isinstance(vetor, Vetor):
            raise TypeError("A subtração só pode ser realizada com outro vetor")
        
        subtracaoAbcissa  = (self.__abcissa) - (vetor.__abcissa)
        subtracaoOrdenada = (self.__ordenada) - (vetor.__ordenada)
        resultado = f'<{subtracaoAbcissa},{subtracaoOrdenada}>'
        return resultado

    def __mul__(self, vetor) :

        if not isinstance(vetor, Vetor):
            raise TypeError("O produto escalar só pode ser realizado com outro vetor")
        
        produtoAbcissa  = self.__abcissa * vetor.__abcissa
        produtoOrdenada = self.__ordenada * vetor.__ordenada
        resultado = (produtoAbcissa) + (produtoOrdenada)
        return resultado
    
    def read_only_Abcissa (self) :
        return f'O valor da abcissa do vetor é : {self.__abcissa}'
    
    def read_only_Ordenada (self) :
        return f'O valor da ordenada do vetor é : {self.__ordenada}'
    
    def read_only_Modulo (self) :
        return f'O valor do modulo do vetor é : {self.__modulo}'

#Instanciando Vetores
vetor1 = Vetor(10,5)
vetor2 = Vetor(2,8)
vetor3 = Vetor(6,6)
vetor4 = Vetor(-2,9)

#Imprimindo Vetores
print('Imprimindo Vetores')
print(vetor1,vetor2,vetor3,vetor4)

#Operaçoes com Vetores
print('Operaçoes entre dois Vetores : (+, -, *)')
print(vetor1 + vetor3)
print(vetor4 - vetor2)
print(vetor1 * vetor2)

#Lendo atributos privados dos Vetores
print(vetor1.read_only_Abcissa())
print(vetor1.read_only_Ordenada())
print(vetor1.read_only_Modulo())