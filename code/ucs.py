# Modelos

ilustracao1 = {'A': {'filhos': ['B', 'C', 'D', 'E'], 'custos': {'B': 4, 'C': 3, 'D': 2, 'E': 10}},
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

# sempre encontra o caminho menos custoso
def ucs(arvore, inicio, objetivo):

    # Fila de prioridade (ordenada)
    fila_prioridades = []

    # adicionar na fila de fila_prioridades
    heapq.heappush(fila_prioridades, (0, (inicio, [inicio])))

