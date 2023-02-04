#Gustavo Brandao Tavares

from problema_01 import Check_Sequencia

#Class Check_Sequencia(N = Quantidade de elementos, * Números da sequencia)
#Verifica se uma sequencia é M-Alterrnada,se True retorna a quantidade de segmentos se False retorna string 'NAO' 


#Exemplos do enunciado
teste_01 = Check_Sequencia(10, [12, 3, 7, 2, 10, 4, 5, 13, 5, 11])
teste_02 = Check_Sequencia(8, [11, 2, 3, 4, 5, 77, 33, 44])
print(teste_01)
print(teste_02)



#Testar de forma dimanica
print("\nVerifique se a sequencia é M-Alternada")

quant_elementos = int(input("Digite a quantidade de números da sequencia : "))

elementos = input('Digite os elementos da sequencia : ')

print("%")

sequen = []

for e in elementos.split(" "):
    if e != ' ':
        sequen.append(int(e))

teste = Check_Sequencia(N = quant_elementos, sequencia=sequen)

print(teste)