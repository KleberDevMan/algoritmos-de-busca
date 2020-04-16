# biblioteca python para ordenar listas
import heapq
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

def ucs(arvore, inicio, objetivo):
    # Fila de prioridade -> ORDENAR
    fila_prioridade = []
    # adicionar na fila de prioridades
    heapq.heappush(fila_prioridade, (0, (inicio, [inicio])))
    nos_visitados = []

    while fila_prioridade:

        # retira da fila de prioridades
        expande = []
        # retira o elemento com menor custo acumulativo
        expande.append(heapq.heappop(fila_prioridade))
        (pai, caminho) = expande[0][1]

        # pega o custo acumulativo
        custo = expande[0][0]
        nos_visitados.append(pai)

        if pai == objetivo:
            resultado = {'caminho': caminho, 'custo': custo,
                         'nos_visitados': nos_visitados}
            return resultado

        filhos = arvore[pai]['filhos']
        for filho in filhos:
            custo_acc = custo + arvore[filho]['custos'][pai]
            # essa estrutura heap já ordena de acorco com o custo acumulado
            heapq.heappush(fila_prioridade, (custo_acc,
                                             (filho, caminho + [filho])))


print('UCS: ', ucs(arvore, 'A', 'H'))

