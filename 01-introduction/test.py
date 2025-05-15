import numpy as np



# terminated = True
# future_q_value = (not terminated) * np.max([1.0, 2.0])
# print(future_q_value)


start_epsilon = 1.0
n_episodes = 100_000
epsilon_decay = start_epsilon / (n_episodes / 2)
print(epsilon_decay)