import random
import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# Criando o ambiente do CartPole
env = gym.make("CartPole-v1")

# Obtendo o número de estados e ações possíveis
n_states = env.observation_space.shape[0]
n_actions = env.action_space.n

# Criando o modelo da rede neural
model = Sequential(
    [
        Dense(24, input_shape=(n_states,), activation="relu"),  # Camada de entrada
        Dense(24, activation="relu"),  # Camada oculta
        Dense(n_actions, activation="linear"),  # Camada de saída
    ]
)

model.compile(loss="mse", optimizer=Adam())  # Configurando o modelo


def dqn(env, num_episodes, batch_size, gamma, epsilon):
    replay_buffer = []  # Buffer para armazenar as experiências
    for episode in range(num_episodes):
        state = env.reset()  # Reiniciando o ambiente para um novo episódio
        done = False

        while not done:
            if np.random.rand() < epsilon:
                action = (
                    env.action_space.sample()
                )  # Exploração: escolhendo uma ação aleatória
            else:
                action = np.argmax(
                    model.predict(np.expand_dims(state, axis=0))
                )  # Exploração: escolhendo a melhor ação com base no modelo

            next_state, reward, done, _ = env.step(
                action
            )  # Executando a ação no ambiente

            # Armazenando a experiência no replay buffer
            replay_buffer.append((state, action, reward, next_state, done))
            state = next_state

            if len(replay_buffer) >= batch_size:
                minibatch = np.array(
                    random.sample(replay_buffer, batch_size)
                )  # Amostrando um minibatch aleatório do replay buffer
                states = np.concatenate(
                    minibatch[:, 0]
                )  # Obtendo os estados do minibatch
                actions = minibatch[:, 1]  # Obtendo as ações do minibatch
                rewards = minibatch[:, 2]  # Obtendo as recompensas do minibatch
                next_states = np.concatenate(
                    minibatch[:, 3]
                )  # Obtendo os próximos estados do minibatch
                dones = minibatch[
                    :, 4
                ]  # Obtendo as informações de episódio terminado do minibatch

                targets = rewards + gamma * (1 - dones) * np.amax(
                    model.predict(next_states), axis=1
                )  # Calculando os targets para a atualização do modelo
                target_vec = model.predict(
                    states
                )  # Obtendo os valores preditos pelo modelo
                target_vec[
                    np.arange(batch_size), actions
                ] = targets  # Atualizando os valores preditos com os targets calculados

                model.fit(
                    states, target_vec, epochs=1, verbose=0
                )  # Atualizando o modelo com os dados do minibatch

    return model


# Treinando o modelo usando DQN
trained_model = dqn(env, num_episodes=1000, batch_size=32, gamma=0.99, epsilon=0.1)
