def make_link(g,node1,node2): #função para construir o gráfico no formato JSOn
    if node1 not in G:
        G[node1]={}
    (G[node1])[node2]=1
    if node2 not in G:
        G[node2]={}
    (G[node2])[node1]=1

G={} #inicializar o grapgh vazio
connections = [('teclado','placa'),('teclado', 'pontos'),('teclado', 'telefone'), ('teclado', 'maos'),
        ('placa','pessoas'),('placa','cadeirante'),
        ('pontos','sucesso!'),
        ('telefone', 'sucesso!'),('telefone', 'orelha'),
        ('maos', 'orelha')] #tuples representing the connections

for x,y in connections:make_link(G,x,y) #construindo o gráfico usando representação de tupla

print(G)

def dfs(G,node,traversed):
    traversed[node]=True #marcar o nó atravessado
    print(traversed, node) 
    # print(traversed) 
    # print(node)

    for neighbour_nodes in G[node]: #pegue um nó vizinho 
        if neighbour_nodes not in traversed: #condição para verificar se o nó vizinho já está visitado
            dfs(G,neighbour_nodes,traversed) #atravessar recursivamente o nó vizinho

def start_traversal(G):
    traversed = {} #dicionário para marcar os nós atravessados
    for node in G.keys(): #G.keys () retorna um nó do gráfico em sua iteração
        # if node not in traversed: #você começa a percorrer o nó raiz apenas se não for visitado 
            dfs(G,node,traversed) #para um gráfico conectado, isso é chamado apenas uma vez

start_traversal(G)