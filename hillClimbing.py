import math
import random


def distancia_euclidiana(cidade1, cidade2):
    x1, y1 = cidade1
    x2, y2 = cidade2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def custo_rota(cidades, rota):
    custo_total = 0.0
    for i in range(len(rota)):
        cidade_atual = cidades[rota[i]]
        proxima_cidade = cidades[rota[(i + 1) % len(rota)]]
        custo_total += distancia_euclidiana(cidade_atual, proxima_cidade)
    return custo_total


def hill_climbing(cidades):
    rota_atual = list(range(len(cidades)))
    # random.shuffle(rota_atual) #define um ponto qualquer como ponto inicial
    random.shuffle(rota_atual[1:]) # define como ponto inicial a primeira tupla (5,5)
    custo_atual = custo_rota(cidades, rota_atual)
    print("Ponto inicial:", cidades[rota_atual[0]])
    for cidade in rota_atual:
        print(cidades[cidade])

    while True:
        vizinhos = []
        for i in range(1, len(cidades)):
            for j in range(i + 1, len(cidades)):
                vizinho = rota_atual.copy()
                vizinho[i:j] = reversed(vizinho[i:j])
                vizinhos.append(vizinho)

        melhor_vizinho = vizinhos[0]
        melhor_custo = custo_rota(cidades, melhor_vizinho)
        for vizinho in vizinhos:
            custo_vizinho = custo_rota(cidades, vizinho)
            if custo_vizinho < melhor_custo:
                melhor_vizinho = vizinho
                melhor_custo = custo_vizinho

        if melhor_custo < custo_atual:
            rota_atual = melhor_vizinho.copy()
            custo_atual = melhor_custo
        else:
            break

    return rota_atual, custo_atual


def hill_climbing_start(cidades):
    melhor_rota, melhor_custo = hill_climbing(cidades)
    print(f"Melhor rota encontrada: {melhor_rota}")
    for cidade_idx in melhor_rota:
        print(cidades[cidade_idx])
    print(f"Custo da melhor rota: {melhor_custo}")