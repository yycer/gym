import gymnasium as gym

# 创建一个强化学习环境对象
env = gym.make("LunarLander-v3", render_mode="human")

# 重置环境，获取初始观测值和信息
observation, info = env.reset()

# 初始化一个布尔变量，用于判断是否结束当前回合
episode_over = False

# 开始一个回合
while not episode_over:
    # 从环境中随机选择一个动作
    action = env.action_space.sample()

    # 执行动作，获取新的观测值、奖励、是否终止、是否截断、环境信息
    observation, reward, terminated, truncated, info = env.step(action)

    # 如果回合结束，则更新回合结束标志
    episode_over = terminated or truncated

# 关闭环境
env.close()