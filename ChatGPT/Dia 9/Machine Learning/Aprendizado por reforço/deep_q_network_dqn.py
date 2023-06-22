import random
import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

env = gym.make("CartPole-v1")
n_states = env.observation_space.shape[0]
n_actions = env.action_space.n

model = Sequential(
    [
        Dense(24, input_shape=(n_states,), activation="relu"),
        Dense(24, activation="relu"),
        Dense(n_actions, activation="linear"),
    ]
)

model.compile(loss="mse", optimizer=Adam())


def dqn(env, num_episodes, batch_size, gamma, epsilon):
    replay_buffer = []
    for episode in range(num_episodes):
        state = env.reset()
        done = False

        while not done:
            if np.random.rand() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(model.predict(np.expand_dims(state, axis=0)))

            next_state, reward, done, _ = env.step(action)

            replay_buffer.append((state, action, reward, next_state, done))
            state = next_state

            if len(replay_buffer) >= batch_size:
                minibatch = np.array(random.sample(replay_buffer, batch_size))
                states = np.concatenate(minibatch[:, 0])
                actions = minibatch[:, 1]
                rewards = minibatch[:, 2]
                next_states = np.concatenate(minibatch[:, 3])
                dones = minibatch[:, 4]

                targets = rewards + gamma * (1 - dones) * np.amax(
                    model.predict(next_states), axis=1
                )
                target_vec = model.predict(states)
                target_vec[np.arange(batch_size), actions] = targets

                model.fit(states, target_vec, epochs=1, verbose=0)

    return model


trained_model = dqn(env, num_episodes=1000, batch_size=32, gamma=0.99, epsilon=0.1)
