import heapq
arvore = {'A': {'h': 50,'filhos': ['B', 'C', 'D', 'E'], 'custos': {'B': 4, 'C': 3, 'D': 2, 'E': 10}},
            'B': {'h' : 9,'filhos': ['F', 'G'], 'custos': {'A': 4, 'F': 5, 'G': 7}},
            'C': {'h': 8,'filhos': ['H'], 'custos': {'A': 3, 'H': 10}},
            'D': {'h' : 7,'filhos': ['H', 'I'], 'custos': {'A': 2, 'H': 12, 'I': 8}},
            'E': {'h' :11,'filhos': ['J'], 'custos': {'A': 7, 'J': 10}},
            'F': {'h': 7,'filhos': [], 'custos': {'B': 5}},
            'G': {'h': 3,'filhos': [], 'custos': {'B': 7}},
            'H': {'h': 0,'filhos': [], 'custos': {'C': 10, 'D': 12}},
            'I': {'h': 13,'filhos': [], 'custos': {'D': 8}},
            'J': {'h' : 15,'filhos': [], 'custos': {'E': 10}}
        }
def gulosa(arvore,node_inicio,objetivo):
    fila = []
    heapq.heappush(fila,(arvore[node_inicio]['h'],(node_inicio,[node_inicio],0)))
    nos_visitados =[]
    while fila:
        expande = []
        expande.append(heapq.heappop(fila))
        (pai,caminho,custo) =expande[0][1]
        nos_visitados.append(pai)
        if pai == objetivo:
            resultado = {'caminho': caminho,'custos':custo,'nos_visitados':nos_visitados}
            return resultado 
        
        filhos = arvore[pai]['filhos']
        for filho in filhos:
            custo_acc = custo + arvore[filho]['custos'][pai]
            heapq.heappush(fila,(arvore[filho]['h'],(filho,caminho + [filho],custo_acc)))

print('gulosa: ',gulosa(arvore,'A','H'))