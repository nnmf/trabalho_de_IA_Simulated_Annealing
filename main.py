import math
import random


def distancia(cidade1, cidade2):
    return math.sqrt((cidade1[0] - cidade2[0]) ** 2 + (cidade1[1] - cidade2[1]) ** 2)


def custo_rota(cidades, rota):
    custo = 0
    for i in range(len(rota)):
        cidade_atual = cidades[rota[i]]
        cidade_proxima = cidades[rota[(i + 1) % len(rota)]]
        custo += distancia(cidade_atual, cidade_proxima)
    return custo


def simulated_annealing(cidades, temperatura_inicial, taxa_resfriamento):
    rota_atual = list(range(len(cidades)))
    random.shuffle(rota_atual)
    custo_atual = custo_rota(cidades, rota_atual)
    temperatura = temperatura_inicial
    while temperatura > 1:
        rota_vizinha = rota_atual.copy()
        i = random.randint(0, len(cidades) - 1)
        j = random.randint(0, len(cidades) - 1)
        rota_vizinha[i], rota_vizinha[j] = rota_vizinha[j], rota_vizinha[i]
        custo_vizinho = custo_rota(cidades, rota_vizinha)
        delta_custo = custo_vizinho - custo_atual
        if delta_custo < 0 or random.random() < math.exp(-delta_custo / temperatura):
            rota_atual = rota_vizinha.copy()
            custo_atual = custo_vizinho
        temperatura *= taxa_resfriamento
    return rota_atual, custo_atual


def main():
    cidades = [(5, 5), (10, 5), (7, 8), (2, 2), (1, 10), (9, 3), (6, 9), (4, 6)]
    temperatura_inicial = 1000
    taxa_resfriamento = 0.99
    melhor_rota, melhor_custo = simulated_annealing(cidades, temperatura_inicial, taxa_resfriamento)
    print("Melhor rota encontrada:", melhor_rota)
    print("Custo da melhor rota:", melhor_custo)


if __name__ == '__main__':
    main()
