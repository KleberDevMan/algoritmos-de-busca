# Programa Python3 para imprimir a travessia do 
# Depth First Search (DFS): Profundidade primeiro

import modelagens as m

percorridos = [] # Guarda os nos visitados
def dfs(estado, destiny, arvore):
    # guarda o nó inicial e o caminho que será percorrido
    pilha = [(estado, [estado])]

    # roda enquanto houver elementos na pilha
    while(pilha):
        # remove o ultimo elemnto da pilha
        (estado, caminho) = pilha.pop()
        percorridos.append(estado)

        # se o estado for igual ao destino retorno o caminho
        if estado == destiny:
            return(caminho)

        # percorre o filhos do estado atual
        for neighbour in reversed(arvore[estado]):
            # adiciona o no a pilha e aos nos visitados
            pilha.append((neighbour,caminho + [neighbour]))


# Graph
caminho = dfs('A', 'E', m.graph)

# atividade 01/04: TORRE MODELAGEM 1
# caminho = dfs('0', '14', m.torre_hanoi)

# atividade 01/04: TORRE MODELAGEM 2
# caminho = dfs('0', '18', m.torre_hanoi_prof)

# atividade 01/04: FIGURA A
# caminho = dfs('A', 'H', m.ilustracao1)

# atividade 01/04: FIGURA B
# caminho = dfs('A', 'E', m.ilustracao2)

# atividade 01/04: FIGURA C
# caminho = dfs('A', 'Q', m.ilustracao2)

# atividade 01/04: FIGURA D
# caminho = dfs('A', 'L', m.ilustracao2)

# RESULTADOS
print('comprimento ({}): '.format(len(caminho)), caminho)
print('nos percorridos ({}): '.format(len(percorridos)), percorridos)