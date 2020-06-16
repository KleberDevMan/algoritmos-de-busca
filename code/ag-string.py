import random

model = input("Digite o modelo: ")
# gera indivíduos com o mesmo tamanho do modelo informado
chromosome_size = len(model)
# tamanho da populacao (stático)
population_size = 100

# critério de parada: tolerância
#   (ou seja, quando encontrar um indivíduo igual ao meu modelo)
#
# entretanto, se for muito custoso, encontrar esse indivíduo,
#   critério de parada: número de gerações
generations = 10000

# Escolha ponderada ??
def weighted_choice(items):
    # calcula o peso total de uma populacao
    total_weight = sum((item[1] for item in items))

    element = random.uniform(0, total_weight)
    
    for item, weight in items:
        if element < weight:
            return item
        element = element - weight
    return item

# caracter randomico
def random_character():
    return chr(int(random.randrange(32, 255, 1)))

# gerar uma populacao inicial
def random_population():
    population = []
    for i in range(population_size):
        chromosome = ""
        for j in range(chromosome_size):
            chromosome += random_character()
        population.append(chromosome)
    return population

# calcula a aptidao de um individuo
def fitness(chromosome):
    fitness = 0
    for i in range(chromosome_size):
        fitness += abs(ord(chromosome[i]) - ord(model[i]))
    return fitness

# mutacao de um individuo
def mutation(chromosome):
    chromosome_outside = ""
    mutation_chance = 100
    for i in range(chromosome_size):
        if int(random.random() * mutation_chance) == 1:
            chromosome_outside += random_character()
        else:
            chromosome_outside += chromosome[i]
    return chromosome_outside

# cruzamento entre dois individuos
def crossover(chromosome1, chromosome2):
    position = int(random.random() * chromosome_size)
    return (chromosome1[:position] + chromosome2[position:], chromosome2[:position] + chromosome1[position:])


# Se o seu módulo não for o programa principal,
#   mas foi importado por outro, então __name__ será "foo",
#   não "__main__" e ele ignorará o corpo da instrução if
if __name__ == "__main__":
    # gera populacao inicial randomica
    population = random_population()

    # for na quantidade max de geracoes
    for generation in range(generations):

        # retorna o numero da geracao e o primeiro individuo dela
        print("Geração %s | População: '%s'" % (generation, population[0]))
        # print("Geração %s | População: '%s' - (%s)" % (generation, population[0], len(population)))
        
        # peso da populacao ??
        weight_population = []

        # se eu atingir a tolerancia (rodar até encontrar um individuo modelo)
        if(population[0] == model):
            break

        # para cada individuo da populacao
        for individual in population:
            # calcula aptidao do individuo
            fitness_value = fitness(individual)

            if fitness_value == 0:
                pair = (individual, 1.0)
            else:
                pair = (individual, 1.0 / fitness_value)

            # adiciona o individuo com seu respectivo indice de aptidao
            weight_population.append(pair)
        
        # inicializa a proxima geracao
        population = []

        # gerando os idividuos da nova polacao 
        #   (selecao + cruzamento + mutacao)
        for i in range(int(population_size)):
            # seleciona dois individuos da populacao anterior
            individual1 = weighted_choice(weight_population)
            individual2 = weighted_choice(weight_population)

            # faz o cruzamento entre esses dois individuos
            individual1, individual2 = crossover(individual1, individual2)

            # adiciona na nova populacao
            #   submentendo cada um a uma possível mutacao
            population.append(mutation(individual1))
            population.append(mutation(individual2))


    fit_string = population[0]
    minimum_fitness = fitness(population[0])

    for individual in population:
        fit_individual = fitness(individual)
        if fit_individual <= minimum_fitness:
            fit_string = individual
            minimum_fitness = fit_individual

    print("População Final: %s" % fit_string)
