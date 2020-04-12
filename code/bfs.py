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

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node, destiny):
  if node == destiny:
    visited.append(node)
  else:
    visited.append(node)
    queue.append(node)

    while queue:
      s = queue.pop(0) 

      for neighbour in graph[s]:
        if neighbour not in visited and destiny not in visited:
          visited.append(neighbour)
          queue.append(neighbour)


# bfs(visited, graph, 'A', 'E')
# bfs(visited, torre_hanoi, '0', '14')
# bfs(visited, torre_hanoi_prof, '0', '18')
# bfs(visited, ilustracao1, 'teclado', 'sucesso')
print('{}'.format(visited))
print('nós visitados: {}'.format(len(visited)))