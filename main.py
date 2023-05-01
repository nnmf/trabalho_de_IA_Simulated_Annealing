from hillClimbing import *
from simulatedAnnealing import *
import time



def main():
    op = 1
    cidades = [(5, 5), (10, 5), (7, 8), (2, 2), (1, 10), (9, 3), (6, 9), (4, 6)]
    while op != 0:
        print(cidades)
        op = int(input("1-Simulated Annelaing\n2-Hill Climbing\n0-Sair\nResposta:"))
        if op == 1:
            print("\n---------- Simulated Annealing ----------\n")
            contagem_inicio = time.time()
            simulated_annealing_start(cidades)
            contagem_fim = time.time()
            tempo_total = contagem_fim - contagem_inicio
            print(f"O algoritmo demorou:{tempo_total}s para completar o percurso")
            print("\n---------- Finalizado ----------\n")
        elif op == 2:
            print("\n---------- Hill Climbing ----------\n")
            contagem_inicio = time.time()
            hill_climbing_start(cidades)
            contagem_fim = time.time()
            tempo_total = contagem_fim - contagem_inicio
            print(f"O algoritmo demorou:{tempo_total}s para completar o percurso")
            print("\n---------- Finalizado ----------\n")
        elif op == 0:
            print("Saindo...")
        else:
            print("Opção inexistente")


if __name__ == '__main__':
    main()
