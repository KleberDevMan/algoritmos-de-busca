# Programa Python3 para imprimir a travessia do 
# Depth First Search (DFS): Profundidade primeiro
import modelagens as m

def dfs(estado, destiny, arvore):
    # guarda o nó inicial e o caminho que será percorrido
    pilha = [(estado, [estado])]
    percorridos = [] # Guarda os nos visitados

    # roda enquanto houver elementos na pilha
    while(pilha):
        # remove o ultimo elemnto da pilha
        (estado, caminho) = pilha.pop()
        percorridos.append(estado)

        # se o estado for igual ao destino retorno o caminho
        if estado == destiny:
            return(caminho, percorridos)

        # percorre o filhos do estado atual
        for neighbour in reversed(arvore[estado]['filhos']):
            # adiciona o no a pilha e aos nos visitados
            pilha.append((neighbour,caminho + [neighbour]))

# atividade 15/04: FIGURA A
# (caminho, percorridos) = dfs('A', 'H', m.ilustracao_a)

# atividade 15/04: FIGURA B
(caminho, percorridos) = dfs('A', 'L', m.ilustracao_b)

# atividade 15/04: FIGURA C
(caminho, percorridos) = dfs('A', 'P', m.ilustracao_c)

# atividade 15/04: FIGURA D
# (caminho, percorridos) = dfs('A', 'R', m.ilustracao_d)

# atividade 15/04: PANQUECAS
# (caminho, percorridos) = dfs('A', 'D', m.panquecas)

# RESULTADOS
print('>>> DFS')
print('comprimento ({}): '.format(len(caminho)), caminho)
print('nos percorridos ({}): '.format(len(percorridos)), percorridos)