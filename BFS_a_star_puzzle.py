from copy import deepcopy

#Direções possíveis na matriz
DIRECTIONS = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}

#Objetivo final
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#Printar todo o puzzle
def print_puzzle(array):
      for row in array:
            print(' '.join(map(str, row)))

#Classe dos nós
class Node:
      def __init__(self, current_node, previous_node, g, h, dir):
            self.current_node = current_node
            self.previous_node = previous_node
            self.g = g
            self.h = h
            self.dir = dir

      #Função de custo
      def f(self):
            return self.g + self.h

#Pega a posição de um elemento
def get_pos(current_state, element):
      for row in range(len(current_state)):
            if element in current_state[row]:
                  return (row, current_state[row].index(element))

#Calcula a distância de manhattan
def manhattanCost(current_state):
      cost = 0
      for row in range(len(current_state)):
            for col in range(len(current_state[0])):
                  pos = get_pos(goal_state, current_state[row][col])
                  cost += abs(row - pos[0]) + abs(col - pos[1])
      return cost

#Pega os nós adjacentes
def getAdjNode(node):
      listNode = []
      emptyPos = get_pos(node.current_node, 0)

      for dir in DIRECTIONS.keys():
            newPos = (emptyPos[0] + DIRECTIONS[dir][0], emptyPos[1] + DIRECTIONS[dir][1])
            if 0 <= newPos[0] < len(node.current_node) and 0 <= newPos[1] < len(node.current_node[0]):
                  newState = deepcopy(node.current_node)
                  newState[emptyPos[0]][emptyPos[1]] = node.current_node[newPos[0]][newPos[1]]
                  newState[newPos[0]][newPos[1]] = 0
                  listNode.append(Node(newState, node.current_node, node.g + 1, manhattanCost(newState), dir))

      return listNode

#Retorna o melhor nó
def getBestNode(openSet):
      firstIter = True
      for node in openSet.values():
            if firstIter or node.f() < bestF:
                  firstIter = False
                  bestNode = node
                  bestF = bestNode.f()
      return bestNode

#Retorna o melhor caminho para o nó final
def buildPath(closedSet):
      node = closedSet[str(goal_state)]
      branch = list()

      while node.dir:
            branch.append({
                  'dir': node.dir,
                  'node': node.current_node
            })
            node = closedSet[str(node.previous_node)]
      branch.append({
            'dir': '',
            'node': node.current_node
      })
      branch.reverse()

      return branch

#Função que vai ser chamada no main
def BFS_main(puzzle):
      open_set = {str(puzzle): Node(puzzle, puzzle, 0, manhattanCost(puzzle), "")}
      closed_set = {}

      while True:
            test_node = getBestNode(open_set)
            closed_set[str(test_node.current_node)] = test_node

            if test_node.current_node == goal_state:
                  return buildPath(closed_set)

            adj_node = getAdjNode(test_node)
            for node in adj_node:
                  if str(node.current_node) in closed_set.keys() or str(node.current_node) in open_set.keys() and open_set[
                        str(node.current_node)].f() < node.f():
                        continue
                  open_set[str(node.current_node)] = node

            del open_set[str(test_node.current_node)]


def print_solution(solution):
      print("POSIÇÃO INICIAL")
      for step in solution:
            print_puzzle(array=step['node'])
            print()
