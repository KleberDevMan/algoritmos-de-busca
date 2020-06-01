import heapq
import math
import numpy as np
from scipy.spatial import distance
import copy
import matplotlib.pyplot as plt
import time
import heapq


def draw(no):
    plt.plot(no[0], no[1], "xc")
    # para simulacao com a tecla esc
    plt.gcf().canvas.mpl_connect('key_release_event',
                                 lambda event: [exit(0) if event.key == 'escape' else None])


def calc_heuristica(inicio, objetivo):
    # numero de passos restantes
    # h = abs(sum(inicio - objetivo))

    # distância euclidiana
    # h = math.sqrt(sum(inicio - objetivo)**2)
    # h = distance.euclidean(inicio, fim)

    # distância de manrratan
    h = distance.cityblock(inicio, fim)

    #

    return h


def astar(grafo, movimento, grid):
    # print('\n\n\n\n\n\n\n\n')

    # g -> custo acumulado
    g = 0
    # h -> heuristica
    h = grafo['ini']['h']
    # f -> função que calcula o valor da heuristica de decisao
    f = h + g

    # Fila de prioridade -> ORDENAR
    fila_prioridade = []
    # adicionar na fila de prioridades
    heapq.heappush(fila_prioridade, (f, (0, ('ini'), [('ini')])))
    # nos_visitados = []
    nos_expandidos = set()
    objetivo = grafo['fim']
    heuristica_error = []

    while fila_prioridade:
        # retira da fila de prioridades
        expande = []
        # retira o elemento com menor custo real
        expande.append(heapq.heappop(fila_prioridade))
        (g, nome_pai, caminho) = expande[0][1]

        pai = grafo[nome_pai]

        # pega o custo real
        f = expande[0][0]

        if np.array_equal(pai['xy'], objetivo['xy']):
            return pai, nos_expandidos, heuristica_error

        # verificar se esse nó ainda não foi expandido
        if (nome_pai not in nos_expandidos):
            # adiciona o nó atual nos nós expandidos
            nos_expandidos.add(nome_pai)

            draw(pai['xy'])

            # controla a frequencia do plot de nós expandidos
            if len(nos_expandidos) % 1 == 0:
                plt.pause(0.001)

            # criar filhos e adicionar na fila de prioridade
            for direcao, mov in movimento.items():
                # definindo um movimento do robô
                filho_xy = np.add(pai['xy'], mov['xy'])

                # Avalia se a heurística é consistente
                #   a partir desse nó filho
                fa = (pai['g'] + pai['h'])
                fc = (pai['g'] + mov['g'] +
                      calc_heuristica(filho_xy, objetivo['xy']))
                if (fa > fc):
                    heuristica_error.append(filho_xy)

                if (all(filho_xy >= grid[0]) and
                        all(filho_xy <= grid[1])):

                    # seta heuristica
                    heu = calc_heuristica(filho_xy, objetivo['xy'])

                    # seta caminho
                    caminho = copy.deepcopy(pai['path'])
                    caminho.append(tuple(filho_xy))

                    # definino valores do filho
                    filho = {'xy': filho_xy,
                             'g': 1,
                             'h': heu,
                             'path': caminho}

                    custo_acc = g + filho['g']

                    # adiciona filho no grafo
                    nome_filho = str(tuple(filho_xy))
                    grafo[nome_filho] = filho

                    # ordeno a fila de acordo com a heuristica

                    f_filho = custo_acc + filho['h']
                    # essa estrutura heap já ordena de acorco com o custo acumulado
                    heapq.heappush(fila_prioridade, (f_filho,
                                                     (custo_acc, nome_filho, caminho)))


def ucs(grafo, movimento, grid):
    # Fila de prioridade -> ORDENAR
    fila_prioridade = []
    # adicionar na fila de prioridades
    heapq.heappush(fila_prioridade, (0, (('ini'), [('ini')])))
    # nos_visitados = []
    nos_expandidos = set()

    objetivo = grafo['fim']

    while fila_prioridade:

        # retira da fila de prioridades
        expande = []
        # retira o elemento com menor custo acumulativo
        expande.append(heapq.heappop(fila_prioridade))
        (nome_pai, caminho) = expande[0][1]
        custo = expande[0][0]

        pai = grafo[nome_pai]

        if np.array_equal(pai['xy'], objetivo['xy']):
            return pai, nos_expandidos, []

        # verificar se esse nó ainda não foi expandido
        if (nome_pai not in nos_expandidos):
            # adiciona o nó atual nos nós expandidos
            nos_expandidos.add(nome_pai)

            # desenha em verde esse nó que foi expandido
            draw(pai['xy'])

            # controla a frequencia do plot de nós expandidos
            if len(nos_expandidos) % 1 == 0:
                plt.pause(0.001)

            # criar filhos e adicionar na fila de prioridade
            for direcao, mov in movimento.items():
                # definindo um movimento do robô
                filho_xy = np.add(pai['xy'], mov['xy'])

                if (all(filho_xy >= grid[0]) and
                        all(filho_xy <= grid[1])):

                    # heu = calc_heuristica(filho_xy,objetivo['xy'])

                    # seta caminho
                    caminho = copy.deepcopy(pai['path'])
                    caminho.append(tuple(filho_xy))

                    # definino valores do filho
                    filho = {'xy': filho_xy,
                             'g': 1,
                             'h': 0,
                             'path': caminho}

                    custo_acc = custo + filho['g']

                    # adiciona filho no grafo
                    nome_filho = str(tuple(filho_xy))
                    grafo[nome_filho] = filho

                    # essa estrutura heap já ordena de acorco com o custo acumulado
                    heapq.heappush(fila_prioridade, (custo_acc,
                                                     (nome_filho, caminho)))


def guloso(grafo, movimento, grid):
    # print('\n\n\n\n\n\n\n\n')
    fila = []
    heapq.heappush(fila, (grafo['ini']['h'], (('ini'), [('ini')], 0)))
    # nos_visitados =[]
    nos_expandidos = set()
    objetivo = grafo['fim']
    heuristica_error = []
    while fila:
        expande = []
        expande.append(heapq.heappop(fila))
        (nome_pai, caminho, custo) = expande[0][1]

        custo = expande[0][0]
        pai = grafo[nome_pai]

        if np.array_equal(pai['xy'], objetivo['xy']):
            return pai, nos_expandidos, heuristica_error

        # verificar se esse nó ainda não foi expandido
        if (nome_pai not in nos_expandidos):
            # adiciona o nó atual nos nós expandidos
            nos_expandidos.add(nome_pai)

            draw(pai['xy'])

            # controla a frequencia do plot de nós expandidos
            if len(nos_expandidos) % 1 == 0:
                plt.pause(0.001)

            # criar filhos e adicionar na fila de prioridade
            for direcao, mov in movimento.items():
                # definindo um movimento do robô
                filho_xy = np.add(pai['xy'], mov['xy'])

                # Avalia se a heurística é consistente
                #   a partir desse nó filho
                fa = (pai['g'] + pai['h'])
                fc = (pai['g'] + mov['g'] +
                      calc_heuristica(filho_xy, objetivo['xy']))
                if (fa > fc):
                    heuristica_error.append(filho_xy)

                if (all(filho_xy >= grid[0]) and
                        all(filho_xy <= grid[1])):

                    # seta heuristica
                    heu = calc_heuristica(filho_xy, objetivo['xy'])

                    # seta caminho
                    caminho = copy.deepcopy(pai['path'])
                    caminho.append(tuple(filho_xy))

                    # definino valores do filho
                    filho = {'xy': filho_xy,
                             'g': 1,
                             'h': heu,
                             'path': caminho}

                    custo_acc = custo + filho['g']

                    # adiciona filho no grafo
                    nome_filho = str(tuple(filho_xy))
                    grafo[nome_filho] = filho

                    # ordeno a fila de acordo com a heuristica
                    # custo_acc = custo + arvore[filho]['custos'][pai]
                    heapq.heappush(
                        fila, (filho['h'], (nome_filho, caminho, custo_acc)))


def bfs(grafo, movimento, grid):
    # print('\n\n\n\n\n\n\n\n')
    fila = [('ini')]
    objetivo = grafo['fim']
    # guarda os nos visitados
    nos_expandidos = set()

    while fila:
        # pop o primeiro caminho da fila
        (no) = fila.pop(0)
        pai = grafo[no]

        # verificar se esse nó é objetivo de
        if np.array_equal(pai['xy'], objetivo['xy']):
            return pai, nos_expandidos, []

        # verificar se esse nó ainda não foi expandido
        if (no not in nos_expandidos):
            # adiciona o nó atual nos nós expandidos
            nos_expandidos.add(no)

            # desenha em verde esse nó que foi expandido
            draw(pai['xy'])

            # controla a frequencia do plot de nós expandidos
            if len(nos_expandidos) % 1 == 0:
                plt.pause(0.001)

            # expandir -> inserir os filhos na pilha
            for direcao, mov in movimento.items():
                # definindo um movimento do robô
                filho_xy = np.add(pai['xy'], mov['xy'])

                # se esse nó filho não ultrapassar os
                #   limites do ambiente, adiciona ele
                #   na pilha...
                if (all(filho_xy >= grid[0]) and
                        all(filho_xy <= grid[1])):

                    # heu = calc_heuristica(filho_xy,objetivo['xy'])

                    # adiciona caminho
                    caminho = copy.deepcopy(pai['path'])
                    caminho.append(tuple(filho_xy))

                    # definino valores do filho
                    filho = {'xy': filho_xy,
                             'g': 0,
                             'h': 0,
                             'path': caminho}

                    # adiciona filho no grafo
                    nome_filho = str(tuple(filho_xy))
                    grafo[nome_filho] = filho

                    # adiciona filho na lista
                    fila.append((nome_filho))

                # se esse nó filho ultrapassar os limites
                #   do ambiente, desconsidera esse nó
                else:
                    continue


def dfs(grafo, movimento, grid):
    # print('\n\n\n\n\n\n\n\n')
    pilha = [('ini')]
    objetivo = grafo['fim']

    nos_expandidos = set()

    while pilha:
        (no) = pilha.pop()
        pai = grafo[no]

        # verificar se esse nó é objetivo de
        if np.array_equal(pai['xy'], objetivo['xy']):
            return pai, nos_expandidos, []  # array de heristica_erros vazio

        # verificar se esse nó ainda não foi expandido
        if (no not in nos_expandidos):
            # adiciona o nó atual nos nós expandidos
            nos_expandidos.add(no)

            # desenha em verde esse nó que foi expandido
            draw(pai['xy'])

            # controla a frequencia do plot de nós expandidos
            if len(nos_expandidos) % 1 == 0:
                plt.pause(0.001)

            # expandir -> inserir os filhos na pilha
            for direcao, mov in movimento.items():
                # definindo um movimento do robô
                filho_xy = np.add(pai['xy'], mov['xy'])

                # se esse nó filho não ultrapassar os
                #   limites do ambiente, adiciona ele
                #   na pilha...
                if (all(filho_xy >= grid[0]) and
                        all(filho_xy <= grid[1])):

                    # heu = calc_heuristica(filho_xy,objetivo['xy'])
                    caminho = copy.deepcopy(pai['path'])
                    caminho.append(tuple(filho_xy))
                    filho = {'xy': filho_xy, 'g': 0, 'h': 0, 'path': caminho}
                    nome_filho = str(tuple(filho_xy))
                    grafo[nome_filho] = filho

                    pilha.append((nome_filho))

                # se esse nó filho ultrapassar os limites
                #   do ambiente, desconsidera esse nó
                else:
                    continue


movimento = {
    'L': {'xy': [1, 0], 'g': 1},
    'N': {'xy': [0, 1], 'g': 1},
    'O': {'xy': [-1, 0], 'g': 1},
    'S': {'xy': [0, -1], 'g': 1}
}

h_error = []

# inicio e objetivo randomico
ini = np.array([1, 1])
fim = np.array([10, 10])
# ini     = np.random.randint(50,size=2)
# fim     = np.random.randint(50,size=2)
heu = calc_heuristica(ini, fim)

grafo = {'ini': {'xy': ini, 'g': 0, 'h': heu, 'path': [tuple(ini)]},
         'fim': {'xy': fim, 'g': math.inf, 'h': 0, 'path': fim}}
grid = np.array([0, 50])

# plota no grafico a posicao inicial e final
plt.plot(ini[0], ini[1], "og")
plt.plot(fim[0], fim[1], "xb")

# algs =  {'astar': astar, 'ucs': ucs,
#            'guloso': guloso, 'bfs': bfs, 'dfs': dfs}

# algs = {'dfs': dfs}
# algs = {'bfs': bfs}
# algs = {'ucs': ucs}
# algs = {'guloso': guloso}
algs = {'astar': astar}

for alg_nome, alg in algs.items():
    tini = time.time()
    ret, no_exps, h_error = alg(grafo, movimento, grid)
    tfim = time.time()
    # print(tfim - tini)

    if(alg_nome == 'guloso' or alg_nome == 'astar'):
        res = {'Algoritmo': alg_nome,
               'cumprimento do caminho': len(ret['path']),
               'expandidos': len(no_exps),
               'tempo': tfim - tini,
               'custo do caminho': ret['g'],
               'heurísticas inconssistentes:': len(h_error)
               }
    else:
        res = {'Algoritmo': alg_nome,
               'cumprimento do caminho': len(ret['path']),
               'expandidos': len(no_exps),
               'tempo': tfim - tini,
               'custo do caminho': ret['g']
               }

    print(res)

    rx = np.array(ret['path'])[:, 0]
    ry = np.array(ret['path'])[:, 1]

    plt.plot(rx, ry, "-r")
    plt.show()
