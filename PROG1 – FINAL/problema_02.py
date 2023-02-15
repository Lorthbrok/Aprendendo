import random

#Verifica sé há um vencedor ou empate
def jogar(jogadas):
    
    #Dicionario com as possiveis opoes de vitoria
    opcoes = {"pedra": "tesoura", "papel": "pedra", "tesoura": "papel"}
    
    vencedor = None
    for jogada in jogadas:
        perdedores = [j for j in jogadas if opcoes[jogada] == j]
        if len(perdedores) == len(jogadas) - 1:
            vencedor = jogada
            break
    return vencedor

n_jogadores = int(input("Digite o número de jogadores: "))
n_partidas = int(input("Digite o número de partidas: "))

#Cria um lista de jogadores e um contador de vitorias
jogadores = []
vitorias = {}
for i in range(n_jogadores):
    jogador = f"Jogador {i+1}"
    jogadores.append(jogador)
    vitorias[jogador] = 0

for partida in range(n_partidas):
    print(f"Partida {partida+1}")
    jogadas = []

    #Adiciona uma escolha para cada jogador
    for jogador in jogadores:
        jogada = random.choice(["pedra", "papel", "tesoura"])
        jogadas.append(jogada)
        print(f"{jogador} escolheu {jogada}")
    
    vencedor = jogar(jogadas)
    if vencedor is None:
        print("Empate!")
    else:
        indice_vencedor = jogadas.index(vencedor)
        jogador_vencedor = jogadores[indice_vencedor]
        vitorias[jogador_vencedor] += 1
        print(f"{jogador_vencedor} ganhou a partida!")

print("Resumo das vitórias:")
for jogador, num_vitorias in vitorias.items():
    print(f"{jogador}: {num_vitorias} vitórias")