# Python3 Programa para imprimir a travessia do 
# Breadth First Search (BFS): Largura primeiro

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

torre_hanoi = {
  '0' : ['1','15'],
  '1' : ['2'],
  '2' : ['3', '17'],
  '3' : ['4'],
  '4' : ['5', '20'],
  '5' : ['6'],
  '6' : ['7', '8'],
  '7' : ['8'],
  '8' : ['9'],
  '9' : ['10'],
  '10' : ['11'],
  '11' : ['12'],
  '12' : ['13'],
  '13' : ['14'],
  '14' : [],
  '15' : ['16'],
  '16' : ['18', '19'],
  '17' : [],
  '18' : [],
  '19' : ['22'],
  '20' : ['24'],
  '21' : ['25'],
  '22' : ['21', '23'],
  '23' : ['26'],
  '24' : ['9', '10'],
  '25' : ['11', '12'],
  '26' : ['13', '14']
}

torre_hanoi_prof = {
  '0' : ['1','19'],
  '1' : ['2'],
  '2' : ['3'],
  '3' : ['4'],
  '4' : ['5'],
  '5' : ['6'],
  '6' : ['7'],
  '7' : ['8'],
  '8' : ['9'],
  '9' : ['10'],
  '10' : ['11'],
  '11' : ['12'],
  '12' : ['13'],
  '13' : ['14'],
  '14' : ['15'],
  '15' : ['16'],
  '16' : ['17'],
  '17' : ['18'],
  '18' : [],
  '19' : ['20'],
  '20' : ['21'],
  '21' : ['22'],
  '22' : ['23'],
  '23' : ['24'],
  '24' : ['25'],
  '25' : ['26'],
  '26' : ['18']
}


ilustracao1 = {
    'A':['B', 'C', 'D', 'E'],
    'B':['F', 'G'],
    'C':['H'],
    'D':['H', 'I'],
    'E':['J'],
    'F':[],
    'G':[],
    'H':[],
    'I':[],
    'J':[]
}

ilustracao2 = {
  'A':['B', 'S'],
  'B':['C', 'G', 'H'],
  'C':['D', 'F'],
  'D':['E'],
  'E':[],
  'F':['E'],
  'G':['E'],
  'H':['F'],
  'I':['J'],
  'J':['K', 'L'],
  'K':[],
  'L':[],
  'M':['N', 'O'],
  'N':['L'],
  'O':['L', 'P'],
  'P':[],
  'Q':[],
  'R':['Q'],
  'S':['I', 'M', 'R']
}

# localiza o caminho mais curto entre 2 nós de um gráfico usando BFS
def bfs_shortest_path(graph, start, goal):
    # acompanha os nós explorados
    explored = []
    # acompanha todos os caminhos a serem verificados
    queue = [[start]]
    percorridos = [start]
 
    # continua em loop até que todos os caminhos possíveis tenham sido verificados
    if start == goal:
        return "Essa foi fácil! Origem = Destino"
 
    # continua em loop até que todos os caminhos possíveis tenham sido verificados
    while queue:
        # pop o primeiro caminho da fila
        path = queue.pop(0)

        # obtem o último nó do caminho
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # passar por todos os nós vizinhos, construir um novo caminho e 
            # coloque-o na fila
            for neighbour in neighbours:
                percorridos.append(neighbour)
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # caminho de retorno se o vizinho for objetivo
                if neighbour == goal:
                    return (new_path, percorridos)
 
            # marcar o nó como explorado
            explored.append(node)
 
    # caso não haja caminho entre os 2 nós
    return "Desculpe, mas não existe um caminho de conexão :("
 
# (comprimento, nos_percorridos) = bfs_shortest_path(graph, 'A', 'D')
# (comprimento, nos_percorridos) = bfs_shortest_path(torre_hanoi, '0', '14') 
# (comprimento, nos_percorridos) = bfs_shortest_path(torre_hanoi_prof, '0', '18')  
# (comprimento, nos_percorridos) = bfs_shortest_path(ilustracao1, 'A', 'H') 

# destino = alvo (E)
(comprimento, nos_percorridos) = bfs_shortest_path(ilustracao2, 'A', 'E') 

# destino = emogi sério (L)
# (comprimento, nos_percorridos) = bfs_shortest_path(ilustracao2, 'A', 'L') 

# destino = emogi triste (Q)
# (comprimento, nos_percorridos) = bfs_shortest_path(ilustracao2, 'A', 'Q') 

print('comprimento ({}): '.format(len(comprimento)), comprimento)
print('nos percorridos ({}): '.format(len(nos_percorridos)), nos_percorridos)