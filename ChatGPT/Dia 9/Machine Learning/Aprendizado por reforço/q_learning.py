import gym
import numpy as np

# Criando o ambiente do CartPole
env = gym.make("CartPole-v1")

# Obtendo o número de estados e ações possíveis
n_states = env.observation_space.shape[0]
n_actions = env.action_space.n

# Inicializando a tabela Q com zeros
Q = np.zeros((n_states, n_actions))


def q_learning(env, num_episodes, alpha, gamma, epsilon):
    for episode in range(num_episodes):
        # Reiniciando o ambiente para um novo episódio
        state = env.reset()
        done = False

        while not done:
            # Selecionando a ação com base na estratégia epsilon-greedy
            if np.random.rand() < epsilon:
                # Exploração: escolhendo uma ação aleatória
                action = env.action_space.sample()
            else:
                # Exploração: escolhendo a melhor ação com base na tabela Q
                action = np.argmax(Q[state].astype(int))

            # Executando a ação e observando o próximo estado, recompensa e se o episódio terminou
            next_state, reward, done, _ = env.step(action)

            # Atualizando a tabela Q com base na equação de Q-Learning
            Q[state, action] += alpha * (
                reward + gamma * np.max(Q[next_state]) - Q[state, action]
            )

            # Atualizando o estado atual para o próximo estado
            state = next_state

    return Q


# Executando o algoritmo de Q-Learning para obter a tabela Q treinada
Q = q_learning(env, num_episodes=1000, alpha=0.5, gamma=0.99, epsilon=0.1)
