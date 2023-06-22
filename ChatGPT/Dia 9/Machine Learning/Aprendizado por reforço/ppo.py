# Importar as bibliotecas necessárias
import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# Criar o ambiente CartPole
env = gym.make("CartPole-v1")

# Definir o número de estados e ações
n_states = env.observation_space.shape[0]
n_actions = env.action_space.n

# Criar o modelo da política (policy)
policy = Sequential(
    [
        Dense(24, input_shape=(n_states,), activation="relu"),
        Dense(24, activation="relu"),
        Dense(n_actions, activation="softmax"),
    ]
)

# Criar o modelo do valor (value)
value = Sequential(
    [
        Dense(24, input_shape=(n_states,), activation="relu"),
        Dense(24, activation="relu"),
        Dense(1, activation="linear"),
    ]
)

# Compilar os modelos da política e do valor
policy.compile(loss="categorical_crossentropy", optimizer=Adam())
value.compile(loss="mse", optimizer=Adam())


# Definir a função do algoritmo PPO
def ppo(env, num_episodes, gamma, epsilon):
    for episode in range(num_episodes):
        state = env.reset()
        done = False

        while not done:
            # Obter a política atual e o valor atual para o estado
            old_policy = policy.predict(np.expand_dims(state, axis=0)).flatten()
            old_value = value.predict(np.expand_dims(state, axis=0))[0]

            # Escolher uma ação com base na política atual
            action = np.random.choice(np.arange(n_actions), p=old_policy)

            # Executar a ação no ambiente e obter o próximo estado, recompensa e informação sobre o término
            next_state, reward, done, _ = env.step(action)

            # Calcular a vantagem (advantage)
            advantage = (
                reward
                + gamma * value.predict(np.expand_dims(next_state, axis=0))[0]
                - old_value
            )

            # Calcular a nova política com base na política atual e no epsilon
            new_policy = policy.predict(np.expand_dims(state, axis=0)).flatten()
            new_policy[action] = (1 - epsilon) * new_policy[
                action
            ] + epsilon * old_policy[action]
            new_policy /= np.sum(new_policy)

            # Treinar o modelo da política com base no estado e na nova política
            policy.fit(
                np.expand_dims(state, axis=0),
                np.expand_dims(new_policy, axis=0),
                verbose=0,
            )

            # Treinar o modelo do valor com base no estado e na recompensa atualizada
            value.fit(
                np.expand_dims(state, axis=0),
                np.expand_dims(
                    reward
                    + gamma * value.predict(np.expand_dims(next_state, axis=0))[0],
                    axis=0,
                ),
                verbose=0,
            )

            # Atualizar o estado atual para o próximo estado
            state = next_state


# Executar o algoritmo PPO
ppo(env, num_episodes=1000, gamma=0.99, epsilon=0.2)
