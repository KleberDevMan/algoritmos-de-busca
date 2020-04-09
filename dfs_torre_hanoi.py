# Programa Python3 para imprimir a travessia do 
# Depth First Search (DFS): Profundidade primeiro
# de um dado gráfico
from collections import defaultdict 

# Esta classe representa um gráfico direcionado usando # representação da lista de adjacências
class Graph: 

	# Constructor 
	def __init__(self): 

		# dicionário padrão para armazenar gráfico
		self.graph = defaultdict(list) 

	# função para adicionar uma aresta ao gráfico
	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	# Uma função usada pelo DFS
	def DFSUtil(self, v, visited): 

		# Marque o nó atual como visitado # e imprima 
		visited[v] = True
		print(v, end = ' ') 

		# Recorrente para todos os vértices # adjacente a este vértice
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.DFSUtil(i, visited) 

	# A função para fazer a travessia do DFS. Usa # recursive DFSUtil () 
	def DFS(self, v): 

		# Marque todos os vértices como não visitados 
		visited = [False] * (len(self.graph)) 

		# Chame a função auxiliar recursiva # para imprimir a travessia do DFS
		self.DFSUtil(v, visited) 

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

print("caminho percorrido DFS a partir do vértice 0:")
g.DFS(0) 

# This code is contributed by Neelam Yadav 
