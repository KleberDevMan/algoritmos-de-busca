# DFS feito pelo Gabriel junto com o professor na aula do dia 15/04/2020

### MODELAGEM ###
arvore = {'A': {'filhos': ['B', 'C', 'D', 'E'], 'custos': {'B': 4, 'C': 3, 'D': 2, 'E': 10}},
          'B': {'filhos': ['F', 'G'], 'custos': {'A': 4, 'F': 5, 'G': 7}},
          'C': {'filhos': ['H'], 'custos': {'A': 3, 'H': 10}},
          'D': {'filhos': ['H', 'I'], 'custos': {'A': 2, 'H': 12, 'I': 8}},
          'E': {'filhos': ['J'], 'custos': {'A': 7, 'J': 10}},
          'F': {'filhos': [], 'custos': {'B': 5}},
          'G': {'filhos': [], 'custos': {'B': 7}},
          'H': {'filhos': [], 'custos': {'C': 10, 'D': 12}},
          'I': {'filhos': [], 'custos': {'D': 8}},
          'J': {'filhos': [], 'custos': {'E': 10}}
          }

import heapq
def dfs(arvore, node_inicio, objetivo):

    # Pilha - O primeiro que entra, ultimo a sair
    # O ultimo que entra, primeiro a sair

    pilha = [(node_inicio, [node_inicio])]
    percorridos = []
    # Enquanto tiver elemento na pilha
    while pilha:
        # Retira o elemento do topo da pilha
        # (pai, caminho)= pilha.pop(0) - BFS
        (pai, caminho) = pilha.pop()
        percorridos.append(pai)

        if pai == objetivo:
            return {'caminho': caminho, 'nos_percorridos': percorridos}
        # Pega os filhos de um determinado pai da arvore
        filhos = arvore[pai]['filhos']

        # Loop que expande cada filho do nó pai
        for filho in filhos:
            pilha.append((filho, caminho + [filho]))


print(dfs(arvore, 'A', 'H'))
