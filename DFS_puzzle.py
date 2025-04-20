# Definição do estado inicial e objetivo
initial_state = [[1, 3, 0], [7, 2, 5], [8, 4, 6]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


# Classe para representar um nó na árvore de busca
class Node:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return self.depth < other.depth

# Função para verificar se um estado é o objetivo
def is_goal(state):
    return state == goal_state

# Função para encontrar a posição do espaço vazio (0)
def find_blank(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

# Função para gerar os possíveis movimentos a partir de um estado
def generate_moves(state):
    moves = []
    blank_position = find_blank(state)
    for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        new_i = blank_position[0] + move[0]
        new_j = blank_position[1] + move[1]
        if 0 <= new_i < len(state) and 0 <= new_j < len(state[0]):
            new_state = [row[:] for row in state]
            new_state[blank_position[0]][blank_position[1]] = state[new_i][new_j]
            new_state[new_i][new_j] = 0
            moves.append(new_state)
    return moves

# Função de busca em profundidade iterativa
def iterative_deepening_dfs(initial_state):
    depth_limit = 0
    while True:
        result = dfs(initial_state, depth_limit)
        if result is not None:
            return result
        depth_limit += 1

# Função de busca em profundidade limitada
def dfs(initial_state, depth_limit):
    visited = set()
    stack = [Node(initial_state)]
    while stack:
        current_node = stack.pop()
        visited.add(tuple(map(tuple, current_node.state)))
        if is_goal(current_node.state):
            return current_node
        if current_node.depth < depth_limit:
            next_moves = generate_moves(current_node.state)
            for move in next_moves:
                if tuple(map(tuple, move)) not in visited:
                    child_node = Node(move, parent=current_node, move=move, depth=current_node.depth + 1)
                    stack.append(child_node)
    return None

# Função para imprimir o caminho da solução
def print_solutionDFS(solution_node):
      solution_path = []
      current_node = solution_node
      while current_node is not None:
            solution_path.append(current_node.state)
            current_node = current_node.parent
      solution_path.reverse()
      for i, state in enumerate(solution_path):
            for row in state:
                  print(row)
            print()

#Função que vai ser chamada no main
def DFS_main():
    # Resolvendo o quebra-cabeça
    solution_node = iterative_deepening_dfs(initial_state)
    if solution_node is not None:
        print("Descoberto na profundidade", solution_node.depth)
        print("Solução encontrada:")
        print_solutionDFS(solution_node)
    else:
        print("Não foi encontrada solução.")
