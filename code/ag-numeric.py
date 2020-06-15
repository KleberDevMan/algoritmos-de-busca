import random

print("Modelo de entrada:")
print("a b c d e f g h i ... j")
print("Digite seu modelo:")
input_model = input()
model = [int(i) for i in input_model.split()]
print("\n")
print("Modelo: {}".format(model))
print("\n")
# gera indivíduos com o mesmo tamanho do modelo informado
individual_size = len(model)
# tamanho da populacao (stático)
population_size = 10
# numero de individuos para um cruzamento
parents = 2
# taxa de mutacao
mutation_probability = 0.5
# numero de geracoes até agora
geracoes = 0

# cria um indivíduo
def individual(min, max):
    return[random.randint(min, max) for i in range(individual_size)]

# cria a populacao randomica
def create_population():
    return[individual(0, 9) for i in range(population_size)]

# mede a aptidao de um individuo
def fitness(individual):
    # inicia com aptidao 0
    fitness = 0
    # se algum dos alelos for igual ao alelo do modelo
    #   ganha um ponto de aptidao
    for i in range(len(individual)):
        if(individual[i] == model[i]):
            fitness += 1
    # retorna a nota
    return fitness

# seleciona alguns individuos e realiza os cruzamentos
#   devolvendo assim uma nova geracao com a mesma quantidade da anterior
def selection_and_crossover(population):
    # procura os que estão mais proximos do modelo
    #   de acordo com a funcao objetivo
    scored = [(fitness(i), i) for i in population]
    scored = [i[1] for i in sorted(scored)]
    population = scored
    selected = scored[(len(scored) - parents):]

    # fazendo o cruzamento:
    #   pega um ponto aleatório do cromossomo
    #   pega pai1 e o pai2, concatena os dois
    #   gera um novo filho e adiciona na nova populacao
    for i in range(len(population) - parents):
        point = random.randint(1, individual_size - 1)
        parent = random.sample(selected, 2)
        population[i][:point] = parent[0][:point]
        population[i][point:] = parent[1][point:]

    # retorna a nova populacao
    return population

# realiza uma mutacao em alguns indivíduos de uma populacao
def mutation(population):
    # percorre a populacao
    for i in range(len(population) - parents):
        # se a taxa de mutacao for maior ou igual a
        #   um número randomico gerado de 0.0 a 0.9 (aleatóriedade na mutacao)
        #   pega um ponto aleatório em um dos individuos e o altera
        if(random.random() <= mutation_probability):
            point = random.randint(0, individual_size - 1)
            new_value = random.randint(1, 9)
            while(new_value == population[i][point]):
                new_value = random.randint(1, 9)
            population[i][point] = new_value

    # retorna a populacao com alguns mutantes
    return population


# cria uma populacao aleatória
population = create_population()
geracoes += 1
print("População Inicial: {}".format(population))
print("\n")

# loop 100 interacaos (critério de parada: número de gerações)
for i in range(100):
    geracoes += 1
    population = selection_and_crossover(population)
    population = mutation(population)


print("População Final: {}".format(population))
print("\n")

print("Número de geracoes até aqui: ", geracoes)
