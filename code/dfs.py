# Programa Python3 para imprimir a travessia do 
# Depth First Search (DFS): Profundidade primeiro

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

percorridos = [] # Guarda os nos visitados

def dfs(node, destiny, arvore):
    # guarda o nó inicial e o caminho que será percorrido
    pilha = [(node, [node])]

    # roda enquanto houver elementos na pilha
    while(pilha):
        # remove o ultimo elemnto da pilha
        (estado, caminho) = pilha.pop()
        percorridos.append(estado)

        # se o estado for igual ao destino retorno o caminho
        if estado == destiny:
            return(caminho)

        # percorre o filhos do estado atual
        for neighbour in arvore[estado]:
            # adiciona o no a pilha e aos nos visitados
            pilha.append((neighbour,caminho + [neighbour]))

# Testando o algoritmo

caminho = dfs('A', 'E', graph)
# caminho = dfs('0', '14', torre_hanoi)
# caminho = dfs('0', '18', torre_hanoi_prof)
# caminho = dfs('A', 'H', ilustracao1)

# destino = alvo (E)
# caminho = dfs('A', 'E', ilustracao2)

# destino = emogi sério (L)
# (comprimento, nos_percorridos) = bfs_shortest_path(ilustracao2, 'A', 'L') 

# destino = emogi triste (Q)
# (comprimento, nos_percorridos) = bfs_shortest_path(ilustracao2, 'A', 'Q')

# Resultado do algoritmo
print('comprimento ({}): '.format(len(caminho)), caminho)
print('nos percorridos ({}): '.format(len(percorridos)), percorridos)