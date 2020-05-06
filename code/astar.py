# Python3 Programa para imprimir a travessia do
# Uniform Cost Search (BFS): Pesquisa de custos uniforme (espande os nós mais baratos)
import modelagens as m

# biblioteca python para ordenar listas
import heapq


def astar(arvore, inicio, objetivo):
    # g -> custo acumulado
    g = 0
    # h -> heuristica
    h = arvore[inicio]['h']
    # f -> função que calcula o valor da heuristica de decisao
    f = h + g

    # Fila de prioridade -> ORDENAR
    fila_prioridade = []
    # adicionar na fila de prioridades
    heapq.heappush(fila_prioridade, (f, (0, inicio, [inicio])))
    nos_visitados = []

    while fila_prioridade:
        # retira da fila de prioridades
        expande = []
        # retira o elemento com menor custo acumulativo
        expande.append(heapq.heappop(fila_prioridade))
        (g, pai, caminho) = expande[0][1]

        # pega o custo acumulativo
        f = expande[0][0]
        nos_visitados.append(pai)

        if pai == objetivo:
            resultado = {'caminho': caminho, 'custo': f,
                         'nos_visitados': nos_visitados}
            return resultado

        filhos = arvore[pai]['filhos']
        for filho in filhos:
            g_acc = g + arvore[filho]['custos'][pai]
            h_filho = arvore[filho]['h']
            f_filho = g_acc + h_filho
            # essa estrutura heap já ordena de acorco com o custo acumulado
            heapq.heappush(fila_prioridade, (f_filho,
                                             (g_acc, filho, caminho + [filho])))

# atividade 15/04: FIGURA A
result = astar(m.ilustracao_a, 'A', 'H')

# atividade 15/04: FIGURA B
# result = astar(m.ilustracao_b, 'A', 'L')

# atividade 15/04: FIGURA C
# result = astar(m.ilustracao_c, 'A', 'P')

# atividade 15/04: FIGURA D
# result = astar(m.ilustracao_d, 'A', 'R')


# atividade 15/04: PANQUECAS
# result = astar(m.panquecas, 'A', 'D')

result_formatado = {
    'caminho ({})'.format(len(result['caminho'])): result['caminho'],
    'custo': result['custo'],
    'nos_visitados ({})'.format(len(result['nos_visitados'])): result['nos_visitados']
}
print('>>> astar')
print(result_formatado)
