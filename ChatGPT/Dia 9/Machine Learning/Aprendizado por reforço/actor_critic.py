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

# Criar o modelo do ator (política)
actor = Sequential(
    [
        Dense(24, input_shape=(n_states,), activation="relu"),
        Dense(24, activation="relu"),
        Dense(n_actions, activation="softmax"),
    ]
)

# Criar o modelo do crítico (função de valor)
critic = Sequential(
    [
        Dense(24, input_shape=(n_states,), activation="relu"),
        Dense(24, activation="relu"),
        Dense(1, activation="linear"),
    ]
)

# Compilar os modelos do ator e crítico
actor.compile(loss="categorical_crossentropy", optimizer=Adam())
critic.compile(loss="mse", optimizer=Adam())


# Definir a função do algoritmo Actor-Critic
def actor_critic(env, num_episodes, gamma):
    for episode in range(num_episodes):
        state = env.reset()
        done = False

        while not done:
            # Prever as probabilidades das ações usando o modelo do ator
            action_probs = actor.predict(np.expand_dims(state, axis=0)).flatten()
            # Escolher uma ação aleatoriamente com base nas probabilidades previstas
            action = np.random.choice(np.arange(n_actions), p=action_probs)

            # Executar a ação no ambiente e obter o próximo estado, recompensa e informação sobre o término
            next_state, reward, done, _ = env.step(action)

            # Calcular o valor do crítico para o estado atual e próximo estado
            critic_value = critic.predict(np.expand_dims(state, axis=0))[0]
            next_critic_value = critic.predict(np.expand_dims(next_state, axis=0))[0]

            # Calcular o alvo de atualização do crítico usando o valor de TD
            td_target = reward + gamma * next_critic_value * (1 - done)
            td_error = td_target - critic_value

            # Calcular o alvo de atualização do ator usando o erro de TD
            actor_target = np.zeros(n_actions)
            actor_target[action] = td_error

            # Treinar o modelo do ator com base no estado e no alvo de atualização do ator
            actor.fit(
                np.expand_dims(state, axis=0),
                np.expand_dims(actor_target, axis=0),
                verbose=0,
            )

            # Treinar o modelo do crítico com base no estado e no alvo de atualização do crítico
            critic.fit(
                np.expand_dims(state, axis=0),
                np.expand_dims(td_target, axis=0),
                verbose=0,
            )

            # Atualizar o estado atual para o próximo estado
            state = next_state


# Executar o algoritmo Actor-Critic
actor_critic(env, num_episodes=1000, gamma=0.99)
