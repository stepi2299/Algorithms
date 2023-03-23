import gym
import numpy as np
import random

EPSILON = 0.2  # value between 0 and 1. 0 greedy strategy, action will be best value in table (exploitation),
                # 1 - random choice - exploration
GAMMA = 0.6
ALPHA = 0.3
mode = "rgb_array"


def action_choice(q_values: np.ndarray, current_state, environment) -> int:
    random_val = random.uniform(0, 1)
    if random_val < EPSILON:
        return environment.action_space.sample()
    else:
        selected_raw = q_values[current_state]
        idxes_list = list(np.where(np.max(selected_raw) == selected_raw)[0])
        return random.choice(idxes_list)


def initialize_q_table(environment) -> np.ndarray:
    return np.zeros((environment.observation_space.n, environment.action_space.n))


def calculating_reward(q_val, immediate_reward, new_state, previous_state, checked_action) -> float:
    return immediate_reward + GAMMA*np.max(q_val[new_state]) - q_val[previous_state, checked_action]


def updating_q_value(q_val, reward, state, new_state, checked_action) -> np.ndarray:
    q_val[state, checked_action] = q_val[state, checked_action] + ALPHA*(reward + GAMMA*np.max(q_val[new_state])-q_val[state, checked_action])
    return q_val

env = gym.make('FrozenLake-v1', render_mode=mode, desc=None, map_name="8x8", is_slippery=True)
observation, info = env.reset(seed=42)
env.render()
q_val = initialize_q_table(env)
state = 0
action_count = 0
tries = 0

while tries < 10000:
    action = action_choice(q_val, state, env)
    action_count += 1
    new_state, reward, terminated, truncated, info = env.step(action)
    # if state == new_state:
    #     reward = -0.2

    if reward == 1:
        reward = 5
    elif terminated is True:
        reward = -0.5


    q_val = updating_q_value(q_val, reward, state, new_state, action)

    if terminated or truncated or action_count >= 200:
        observation, info = env.reset()
        action_count = 0
        tries += 1

    state = new_state

wins = 0
action_count = 0
tries = 0

while tries < 1000:
    action = action_choice(q_val, state, env)
    action_count += 1
    new_state, reward, terminated, truncated, info = env.step(action)
    # if state == new_state:
    #     reward = -0.2

    if reward == 1:
        reward = 5
        wins += 1
    elif terminated is True:
        reward = -0.5


    q_val = updating_q_value(q_val, reward, state, new_state, action)

    if terminated or truncated or action_count >= 200:
        observation, info = env.reset()
        action_count = 0
        tries += 1

    state = new_state

print(f"Percentage of winning in test set: {(wins/tries)*100} %")
print(f"All test tries: {tries}")
print(f"All wins in test series: {wins}")

env.close()