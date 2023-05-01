from hillClimbing import *
from simulatedAnnealing import *


def main():
    op = 1
    cidades = [(5, 5), (10, 5), (7, 8), (2, 2), (1, 10), (9, 3), (6, 9), (4, 6)]
    while op != 0:
        print(cidades)
        op = int(input("1-Simulated Annelaing\n2-Hill Climbing\n0-Sair\nResposta:"))
        if op == 1:
            print("\n---------- Simulated Annealing ----------\n")
            simulated_annealing_start(cidades)
            print("\n---------- Finalizado ----------\n")
        elif op == 2:
            print("\n---------- Hill Climbing ----------\n")
            hill_climbing_start(cidades)
            print("\n---------- Finalizado ----------\n")
        elif op == 0:
            print("Saindo...")
        else:
            print("Opção inexistente")


if __name__ == '__main__':
    main()
