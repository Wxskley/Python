# Importar as bibliotecas necessárias
from deap import base, creator, tools, algorithms
import random
import gym

# Criar o ambiente CartPole
env = gym.make("CartPole-v1")

# Definir o número de estados e ações
n_states = env.observation_space.shape[0]
n_actions = env.action_space.n

# Criar os tipos Fitness e Individual usando a biblioteca DEAP
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Criar a caixa de ferramentas do DEAP
toolbox = base.Toolbox()

# Registrar a função que gera um valor aleatório para um atributo
toolbox.register("attribute", random.randint, 0, n_actions - 1)

# Registrar a função que cria um indivíduo com base nos atributos gerados
toolbox.register(
    "individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=n_states
)

# Registrar a função que cria uma população de indivíduos
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


# Definir a função de avaliação de um indivíduo
def evaluate(individual):
    total_reward = 0
    state = env.reset()
    done = False

    while not done:
        # Selecionar a ação do indivíduo com base no estado atual
        action = individual[state[0]]
        # Executar a ação no ambiente e obter o próximo estado, recompensa e informação sobre o término
        next_state, reward, done, _ = env.step(action)
        # Atualizar a recompensa total acumulada
        total_reward += reward
        # Atualizar o estado atual para o próximo estado
        state = next_state

    return total_reward


# Registrar a função de avaliação no DEAP
toolbox.register("evaluate", evaluate)

# Registrar os operadores genéticos: cruzamento, mutação e seleção
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=n_actions - 1, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

# Criar uma população inicial de indivíduos
population = toolbox.population(n=100)

# Executar o algoritmo genético para evoluir a população
best_individuals = algorithms.eaSimple(
    population, toolbox, cxpb=0.5, mutpb=0.1, ngen=50
)

# Selecionar o melhor indivíduo da população final
best_individual = tools.selBest(best_individuals, k=1)[0]
