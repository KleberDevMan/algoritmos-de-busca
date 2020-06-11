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

def viola(obs, grid, x, y):
    if x >= grid[0] and x < grid[1] and y >= grid[0] and y < grid[1]:
        for i in range(0, len(obs['ox'])):
            if x == obs['ox'][i] and y == obs['oy'][i]:
                return True
        return False
    return True

def calc_heuristica(inicio, objetivo, h_pai=0):
    if h_pai == 0:
        # Número de passos até o objetivo
        # h = sum(objetivo - inicio)

        # Distância Euclidiana
        # h = distance.euclidean(inicio, fim)

        # Distância de Manhattan
        # h = math.sqrt(sum(objetivo - inicio)**2)
        h = distance.cityblock(inicio, fim)

        return h
    else:
        # Heurística inconssistente
        h = -1

        return h

def astar(grafo, movimento, grid, obs):
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

                # Verifica se não ultrapassou barreiras do grid
                #   e se não é um nó obstaculo
                if viola(obs, grid, filho_xy[0], filho_xy[1]) == False:

                    # seta heuristica
                    heu = calc_heuristica(filho_xy, objetivo['xy'])

                    # Avalia se a heurística é consistente
                    #   a partir desse nó filho
                    fa = (pai['g'] + pai['h'])
                    fc = (pai['g'] + mov['g'] + heu)
                    if (fa > fc):
                        heuristica_error.append(filho_xy)

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

def guloso(grafo, movimento, grid, obs):
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

                # Verifica se não ultrapassou barreiras do grid
                #   e se não é um nó obstaculo
                if viola(obs, grid, filho_xy[0], filho_xy[1]) == False:

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

movimento = {
    'L': {'xy': [1, 0], 'g': 1},
    'N': {'xy': [0, 1], 'g': 1},
    'O': {'xy': [-1, 0], 'g': 1},
    'S': {'xy': [0, -1], 'g': 1}
}

h_error = []

# inicio e objetivo statico
ini = np.array([15, 15])
fim = np.array([35, 45])
heu = calc_heuristica(ini, fim)
grid = np.array([0, 50])

ox, oy = [], []

# posicoes dos obstaculos
for i in range(0, 50):
    ox.append(i)
    oy.append(0)
for i in range(0, 50):
    ox.append(50.0)
    oy.append(i)
for i in range(0, 51):
    ox.append(i)
    oy.append(50.0)
for i in range(0, 51):
    ox.append(0)
    oy.append(i)
for i in range(0, 40):
    ox.append(20.0)
    oy.append(i)
for i in range(0, 40):
    ox.append(40.0)
    oy.append(50.0 - i)


grafo = {'ini': {'xy': ini, 'g': 0, 'h': heu, 'path': [tuple(ini)]},
         'fim': {'xy': fim, 'g': math.inf, 'h': 0, 'path': fim}}

obs = {'ox': ox, 'oy': oy}

# plota no grafico a posicao os obstaculos, 
#   a posicao inicial e final
plt.plot(ox, oy, ".k")
plt.plot(ini[0], ini[1], "og")
plt.plot(fim[0], fim[1], "xb")
# plt.show()

# algs = {'guloso': guloso}
algs={'astar': astar}


for alg_nome, alg in algs.items():
    tini = time.time()
    ret, no_exps, h_error = alg(grafo, movimento, grid, obs)
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
