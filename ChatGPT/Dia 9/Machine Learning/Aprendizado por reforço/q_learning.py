import gym
import numpy as np

env = gym.make("CartPole-v1")
n_states = env.observation_space.shape[0]
n_actions = env.action_space.n

Q = np.zeros((n_states, n_actions))


def q_learning(env, num_episodes, alpha, gamma, epsilon):
    for episode in range(num_episodes):
        state = env.reset()
        done = False

        while not done:
            if np.random.rand() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state].astype(int))

            next_state, reward, done, _ = env.step(action)

            Q[state, action] += alpha * (
                reward + gamma * np.max(Q[next_state]) - Q[state, action]
            )

            state = next_state

    return Q


Q = q_learning(env, num_episodes=1000, alpha=0.5, gamma=0.99, epsilon=0.1)
