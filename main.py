from DFS_puzzle import DFS_main
from BFS_a_star_puzzle import BFS_main, print_solution

def main():
      print("Escolha o algoritmo de busca:")
      print("1. Busca em Profundidade (DFS)")
      print("2. A* (BFS)")
      escolha = int(input("Digite o número correspondente ao algoritmo desejado: "))

      if escolha == 1:
            #Para definir o puzzle inicial, vá até o arquivo DFS_puzzle.py e altere na linha 2
            DFS_main()
            
      elif escolha == 2:
            #Defina aqui o puzzle inicial do BFS
            solution = BFS_main([[6, 2, 8],
                                 [4, 7, 1],
                                 [0, 3, 5]])
            
            print_solution(solution)
      else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()