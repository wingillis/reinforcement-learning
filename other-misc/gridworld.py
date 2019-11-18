import gym
import time
import random
import gym_minigrid
import numpy as np

from gym_minigrid.wrappers import FlatObsWrapper

# simplest env: MiniGrid-Empty-5x5-v0
def reset_env(env):
    env.reset()
    if hasattr(env, 'mission'):
        print('Mission:', env.mission)


def main():
    env = gym.make('MiniGrid-Empty-6x6-v0')
    reset_env(env)

    # so I can see it
    renderer = env.render('human')

    actions = list(env.actions.__members__.values())[:3]
    print(actions)

    for _ in range(400):
        action = random.choice(actions)
        obs, reward, done, info = env.step(action)
        print(obs['direction'])
        env.render('human')
        if done:
            print(reward)
            print('done!')
            return
        time.sleep(0.2)


if __name__ == "__main__":
    main()