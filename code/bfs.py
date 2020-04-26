# Python3 Programa para imprimir a travessia do 
# Breadth First Search (BFS): Largura primeiro
import modelagens as m

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
 

# Graph
(comprimento, nos_percorridos) = bfs_shortest_path(m.graph, 'A', 'D')

# atividade 01/04: TORRE MODELAGEM 1
# (comprimento, nos_percorridos) = bfs_shortest_path(m.torre_hanoi, '0', '14')
 
# atividade 01/04: TORRE MODELAGEM 2
# (comprimento, nos_percorridos) = bfs_shortest_path(m.torre_hanoi_prof, '0', '18')  



# atividade 01/04: FIGURA A
# (comprimento, nos_percorridos) = bfs_shortest_path(ilustracao1, 'A', 'H') 

# atividade 01/04: FIGURA B
# (comprimento, nos_percorridos) = bfs_shortest_path(m.ilustracao2, 'A', 'E') 

# atividade 01/04: FIGURA C
# (comprimento, nos_percorridos) = bfs_shortest_path(m.ilustracao2, 'A', 'Q') 

# atividade 01/04: FIGURA D
# (comprimento, nos_percorridos) = bfs_shortest_path(m.ilustracao2, 'A', 'L') 

print('comprimento ({}): '.format(len(comprimento)), comprimento)
print('nos percorridos ({}): '.format(len(nos_percorridos)), nos_percorridos)