# Algoritmo Genético:
#   1. Inserir um modelo ideal de individuo (string).
#   2. Encontrar uma populacao como indivíduos que se assemelhem ao modelo.
#   
#   Critério de parada: tolerância
#       (ou seja, quando encontrar um indivíduo igual ao meu modelo)
#   entretanto, se for muito custoso encontrar esse indivíduo:
#       Critério de parada: número de gerações
#
#   Códigio referência: https://github.com/anapaulamendes/my-talks-and-workshops/tree/master/python-brasil-2018
import random

# pede o modelo
model = input("Digite o modelo: ")


# Pega o tamanho do modelo
#   (algoritmo trabalha com indivíduos com o mesmo tamanho do modelo informado)
chromosome_size = len(model)
# tamanho da populacao (stático)
population_size = 100
# Se o critério de parada for número de gerações
generations = 10000

# Escolha ponderada: escolhe um individuo com base em seu peso. 
#   pego um valor randomico dentro do peso total. 
#   vou escolher um individuo que esteja acima desse valor. 
#   Uma espécie de torneio. 
#   Entretanto, aqueles com o peso maior são os que têm mais chances     
def weighted_choice(items):
    # somo todos os pesos
    total_weight = sum((item[1] for item in items))

    # pego um valor_randomico de zero até o peso total
    element = random.uniform(0, total_weight)
    
    # para cada individuo
    for item, weight in items:
        # verifico se seu peso é maior que o valor_randomico
        if element < weight:
            # retorno esse individuo
            return item
        
        # senao, decremento o valor_randomico
        element = element - weight

    return item

# caracter randomico
def random_character():
    return chr(int(random.randrange(32, 255, 1)))

# gerar uma populacao inicial randomica
def random_population():
    population = []
    # populacao com tamanho estático
    for i in range(population_size):
        chromosome = ""
        # individuo com tamanho estático
        for j in range(chromosome_size):
            chromosome += random_character()
        population.append(chromosome)

    # retorna populacao
    return population

# calcula a aptidao de um individuo
def fitness(chromosome):
    fitness = 0
    for i in range(chromosome_size):
        # quanto mais longe o unicode da letra do individuo 
        #   estiver da respectiva letra do modelo, mais peso ele ganha
        fitness += abs(ord(chromosome[i]) - ord(model[i]))
    return fitness

# mutacao em um individuo
#   conta com um certo grau de aleatoriedade
def mutation(chromosome):
    chromosome_outside = ""
    mutation_chance = 100

    # para cada caracteristica do individuo
    for i in range(chromosome_size):
        # se ocorrer a conicidencia de um numero randomico ser 1
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
#   mas foi importado por outro, então __name__ será "ag-string",
#   não "__main__" e ele ignorará o corpo da instrução if
if __name__ == "__main__":
    # gera populacao inicial randomica
    population = random_population()

    # for na quantidade max de geracoes
    for generation in range(generations):

        # retorna o numero da geracao e o primeiro individuo dela
        print("Geração %s | População: '%s'" % (generation, population[0]))
        
        # populacao com o peso (aptidao) de cada um já atrelado
        weight_population = []

        # se eu atingir a tolerancia (encontrar um individuo modelo)
        if(population[0] == model):
            break

        # para cada individuo da populacao
        for individual in population:
            # calcula aptidao do individuo. 
            #   Quanto mais longe do modelo, 
            #   maior é o fitness_value dele (valor de aptidao)
            fitness_value = fitness(individual)

            # atribui um peso ao individuo de acordo com o fitness_value 
            if fitness_value == 0:
                pair = (individual, 1.0)
            else:
                # os que tem um fitness_value alto serao penalizados aqui, 
                #   na hora de calcular o seu peso.
                #   pelo fato de ser um divisao, os que tiverem um maior fitness_value
                #   terao um menor peso. Isso irá prejudicá-lo na hora da selecao torneio
                pair = (individual, 1.0 / fitness_value)

            # adiciona o individuo com seu respectivo peso na lista de populacao com peso
            weight_population.append(pair)
        
        # inicializa a proxima geracao
        population = []

        # gerando os idividuos da nova polacao 
        #   (selecao + cruzamento + mutacao)
        for i in range(int(population_size)):
            # seleciona (torneio) dois individuos como base no seu peso
            individual1 = weighted_choice(weight_population)
            individual2 = weighted_choice(weight_population)

            # faz o cruzamento entre esses dois individuos
            individual1, individual2 = crossover(individual1, individual2)

            # adiciona na nova populacao
            #   submentendo cada um a uma possível mutacao (aleatoriedade, pode ou não acontecer)
            population.append(mutation(individual1))
            population.append(mutation(individual2))

    # pega o primeiro individo da populacao
    fit_string = population[0]
    
    # pega o valor de aptidao desse primeiro individuo
    minimum_fitness = fitness(population[0])

    # para cada individuo dessa nova geracao
    for individual in population:
        # pega o valor de aptidao do individuo
        fit_individual = fitness(individual)

        # se esse individuo ta com uma fitness_value mais baixo, 
        #   mais baixo que os outros (ou seja, se parece mais com o modelo) 
        if fit_individual <= minimum_fitness:
            # pego o individuo
            fit_string = individual
            # pego o peso dele
            minimum_fitness = fit_individual

    # exibo o individo da populacao mais parecido com o modelo
    print("População Final: %s" % fit_string)
