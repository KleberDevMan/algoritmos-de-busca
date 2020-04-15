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
    'teclado':['placa', 'pontos', 'telefone', 'maos'], 
    'placa':['pessoas', 'cadeirante'],
    'pessoas':[],
    'cadeirante':[],
    'pontos':['sucesso'],
    'sucesso':[],
    'telefone':['sucesso', 'orelha'],
    'orelha':[],
    'maos':['orelha']
}

visited = [] # Guarda os nos visitados

def dfs(node, destiny, arvore):
    # guarda o nó inicial e o caminho que será percorrido
    pilha = [(node, [node])]

    # enquanto houver elementos na pilha
    while(pilha):
        # remove o ultimo elemnto da pilha
        (estado, caminho) = pilha.pop()
        
        # percorre o filhos do estado atual
        for neighbour in arvore[estado]:

            # se o filho for o no procurado, retorna o caminho
            if neighbour == destiny:
                return(caminho + [neighbour])
            else: # senao, adiciona o no a pilha e aos nos visitados
                pilha.append((neighbour,caminho + [neighbour]))
                visited.append(neighbour)

caminho = dfs('A', 'E', graph)
print('{}'.format(visited))
print('nós visitados: {}'.format(len(visited)))

print('{}'.format(caminho))
print('caminho: ', len(caminho))