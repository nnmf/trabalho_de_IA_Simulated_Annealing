import math
import random


# calculo a distância euclidiana
def distancia_euclidiana(cidade1, cidade2):
    return math.sqrt((cidade1[0] - cidade2[0]) ** 2 + (cidade1[1] - cidade2[1]) ** 2)


# calculo o custo da rota
def custo_rota(cidades, rota):
    custo = 0
    for i in range(len(rota)):
        cidade_atual = cidades[rota[i]]
        cidade_proxima = cidades[rota[(i + 1) % len(rota)]]
        custo += distancia_euclidiana(cidade_atual, cidade_proxima)
    return custo


def simulated_annealing(cidades, temperatura_inicial, taxa_resfriamento):
    rota_atual = list(range(len(cidades)))
    random.shuffle(rota_atual) #define um ponto qualquer como ponto inicial
    # random.shuffle(rota_atual[1:])  # define como ponto inicial a primeira tupla (5,5)
    rota_atual = rota_atual
    custo_atual = custo_rota(cidades, rota_atual)
    temperatura = temperatura_inicial
    print("Ponto inicial:", cidades[rota_atual[0]])
    for cidade in rota_atual:
        print(cidades[cidade])

    while temperatura > 1:
        rota_vizinha = rota_atual.copy()
        i = random.randint(0, len(cidades) - 1)
        j = random.randint(0, len(cidades) - 1)
        rota_vizinha[i], rota_vizinha[j] = rota_vizinha[j], rota_vizinha[i]
        custo_vizinho = custo_rota(cidades, rota_vizinha)
        delta_custo = custo_vizinho - custo_atual #checando se a rota vizinha é menor que a atual
        # se for menor que a atual eu a aceito ou Se um número aleatório entre 0 e 1 for menor que a exponencial de
        # (-delta_custo / temperatura), então a solução pior (vizinha) será aceita, isso significa que com o passar do
        # tempo ele se torna mais seletivo
        if delta_custo < 0 or random.random() < math.exp(-delta_custo / temperatura):
            rota_atual = rota_vizinha.copy()
            custo_atual = custo_vizinho
        temperatura *= taxa_resfriamento
        #print(temperatura)
    return rota_atual, custo_atual


def simulated_annealing_start(cidades):
    temperatura_inicial = 1000
    taxa_resfriamento = 0.99
    melhor_rota, melhor_custo = simulated_annealing(cidades, temperatura_inicial, taxa_resfriamento)
    print(f"Melhor rota encontrada: {melhor_rota}")  # mostro os índices da melhor rota e depois imprimo elas
    for cidade_idx in melhor_rota:
        print(cidades[cidade_idx])
    print(f"Custo da melhor rota: {melhor_custo}")