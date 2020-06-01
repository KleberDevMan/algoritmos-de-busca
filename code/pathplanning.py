import heapq
import math
import numpy as np
from scipy.spatial import distance
import copy
import matplotlib.pyplot as plt
import time

def draw(no):
    plt.plot(no[0], no[1], "xc")
    # para simulacao com a tecla esc
    plt.gcf().canvas.mpl_connect('key_release_event',
        lambda event: [exit(0) if event.key == 'escape' else None])

def calc_heuristica(inicio, objetivo):
    heuristica = 0
    return heuristica

def astar(grafo, movimento, grid):
    pass

def ucs(grafo, movimento, grid):
    pass

def guloso(grafo, movimento, grid):
    pass

def bfs(grafo, movimento, grid):
    fila = [('ini')]
    objetivo = grafo['fim']
    # guarda os nos visitados
    nos_expandidos  = set()

    # verificar se esse nó é objetivo
    if np.array_equal(grafo['ini']['xy'], objetivo['xy']):
        print(">> Essa foi fácil! Origem = Destino")
        return grafo['ini'], nos_expandidos


    while fila:
        # pop o primeiro caminho da fila
        (no) = fila.pop(0)
        pai = grafo[no]

        # verificar se esse nó é objetivo de
        if np.array_equal(pai['xy'], objetivo['xy']):
            return pai, nos_expandidos

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
    pilha           = [('ini')]
    objetivo        = grafo['fim']

    nos_expandidos  = set()    
    
    while pilha:
        (no)    = pilha.pop()
        pai     = grafo[no]

        # verificar se esse nó é objetivo de
        if np.array_equal(pai['xy'], objetivo['xy']):
            return pai, nos_expandidos

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

                # Avalia se a heurística é consistente
                #   a partir desse nó filho
                fa = (pai['g'] + pai['h'])
                fc = (pai['g'] + mov['g'] + calc_heuristica(filho_xy,objetivo['xy'])) 
                if (fa > fc):
                    print("Heurística não é consistente!")

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
                'L': {'xy': [1,0], 'g': 1},
                'N': {'xy': [0,1], 'g': 1},
                'O': {'xy': [-1,0], 'g': 1},
                'S': {'xy': [0,-1], 'g': 1}
            }

### inicio e objetivo randomico
ini   = np.array([10,10])
fim   = np.array([2,2])
# ini     = np.random.randint(50,size=2)
# fim     = np.random.randint(50,size=2)
heu     = calc_heuristica(ini,fim)

grafo   = { 'ini': {'xy': ini, 'g': 0, 'h': heu, 'path': [tuple(ini)]},
          'fim': {'xy': fim, 'g': math.inf, 'h': 0, 'path': fim}}
grid    = np.array([0,50])

### plota no grafico a posicao inicial e final
plt.plot(ini[0], ini[1], "og")
plt.plot(fim[0], fim[1], "xb")

#algs =  {'astar': astar, 'ucs': ucs, 
#            'guloso': guloso, 'bfs': bfs, 'dfs': dfs}

algs = {'dfs': dfs}
# algs = {'bfs': bfs}
# algs = {'ucs': ucs}

for _, alg in algs.items():
    tini            = time.time()
    ret, no_exps    = alg(grafo, movimento, grid)
    tfim            = time.time()
    # print(tfim - tini)    

    res = { 'cumprimento do caminho': len(ret['path']), 
            'expandidos': len(no_exps), 
            'tempo': tfim - tini,
            'custo do caminho': ret['g']}

    print(res)

    rx = np.array(ret['path'])[:,0]
    ry = np.array(ret['path'])[:,1]

    plt.plot(rx, ry, "-r")
    plt.show()
