# Python3 Programa para imprimir a travessia de 
# Breadth First Search (BFS): Largura primeiro
# de dado gráfico
from collections import defaultdict 

# Esta classe representa um gráfico direcionado
# usando representação de lista de adjacências
class Graph: 

	# Constructor 
	def __init__(self): 

		# dicionário padrão para armazenar gráficos 
		self.graph = defaultdict(list) 

	# função para adicionar uma aresta ao gráfico
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# Função para imprimir um BFS do gráfico 
	def BFS(self, s): 

		# Marque todos os vértices como não visitados 
		visited = [False] * (len(self.graph)) 

		# criar uma fila para BFS 
		queue = [] 

		# Marque o nó de origem como # visitado e enfileirá-lo 
		queue.append(s) 
		visited[s] = True

		while queue: 

			# Remover da fila um vértice de 
            # fila e imprima 
			s = queue.pop(0) 
			print (s, end = " ") 

			# Obter todos os vértices adjacentes do 
            # vértices desenfileirados s. Se um adjacente 
            # não foi visitado, marque-o 
            # visitado e enfileirá-lo 
			for i in self.graph[s]: 
				if visited[i] == False: 
					queue.append(i) 
					visited[i] = True

# Testando o codigo 

# criando o grafico 
g = Graph() 
# adiciona arestas para o estado 0
g.addEdge(0, 1) 
g.addEdge(0, 2) 

# adiciona arestas para o estado 1
g.addEdge(1, 0) 
g.addEdge(1, 2)

# adiciona arestas para o estado 2
g.addEdge(2, 1) 
g.addEdge(2, 0)
g.addEdge(2, 3)

# adiciona arestas para o estado 3
g.addEdge(3, 2)
# ...


print ("caminho percorrido DFS a partir do vértice 0:") 
g.BFS(0) 

# This code is contributed by Neelam Yadav 
