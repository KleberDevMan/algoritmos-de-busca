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


def viola(obs, grid, x, y):
    if x >= grid[0] and x < grid[1] and y >= grid[0] and y < grid[1]:
        for i in range(0, len(obs['ox'])):
            if x == obs['ox'][i] and y == obs['oy'][i]:
                return True
        return False
    return True


def move(no, obs, grafo, movimento, grid):
    sol, status = backtracking(no, obs, grafo, movimento, grid)

    if status == False:
        print("Solução não existe!")
        return sol, False

    sol['g'] = len(sol['path'])
    return sol, True


def backtracking(no, obs, grafo, movimento, grid):
    # if (x, y é o objetivo) return True para sair da recursão
    if no['xy'][0] == grafo['fim']['xy'][0] and no['xy'][1] == grafo['fim']['xy'][1]:
        return no, True

    if viola(obs, grid, no['xy'][0], no['xy'][1]) == False:

        draw(no['xy'])
        plt.pause(0.001)

        moves = 0
        for _, mov in movimento.items():
            filho_xy = np.add(no['xy'], mov['xy'])
            print(filho_xy)
            moves += 1

            cam = copy.deepcopy(no['path'])
            cam.append(tuple(filho_xy))
            filho = {'xy': filho_xy, 'g': 0, 'h': 0, 'path': cam}

            sol, status = backtracking(filho, obs, grafo, movimento, grid)
            if status == True:
                return sol, status

            else:
                if moves >= 2:
                    # se nenhum dos movimentos funciona então
                    # # BACKTRACK: retira essa opção da lista de opções
                    obs['ox'].append(no['xy'][0])
                    obs['oy'].append(no['xy'][1])

        return no, False

    else:
        return no, False


movimento = {'L': {'xy': [1, 0], 'g': 1},
             'N': {'xy': [0, 1], 'g': 1},
             'O': {'xy': [-1, 0], 'g': 1},
             'S': {'xy': [0, -1], 'g': 1}
             }

# inicio e objetivo randomico
#ini = np.random.randint(50,size=2)
#fim = np.random.randint(50,size=2)
ini = np.array([15, 15])
fim = np.array([35, 45])
heu = 0
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

plt.plot(ox, oy, ".k")
plt.plot(ini[0], ini[1], "og")
plt.plot(fim[0], fim[1], "xb")

# Backtracking
tini = time.time()
ret, status = move(grafo['ini'], obs, grafo, movimento, grid)
no_exps = len(ret['path'])
tfim = time.time()
print(tfim - tini)

res = {'cumprimento do caminho': len(ret['path']),
       'visitados': no_exps,
       'tempo': tfim - tini,
       'custo do caminho': ret['g']}

print(res)

rx = np.array(ret['path'])[:, 0]
ry = np.array(ret['path'])[:, 1]

plt.plot(rx, ry, "-r")
plt.show()
