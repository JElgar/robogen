import os
import subprocess
from dataclasses import dataclass

import gym
from stable_baselines3 import PPO

# Stealing code from https://github.com/talregev/gym-webots/blob/master/gym_webots/envs/webots_env.py
@dataclass
class WebotsConfig:
    port: int = 4000
    world_file = os.path.join(
        os.path.dirname(__file__), "webots", "worlds", "labsheet_x.wbt"
    )


class WebotsEnv(gym.Env):
    def __init__(self):
        self.config = WebotsConfig()
        print(f"Webots Stream=http://localhost:{self.config.port}")

        # port_param = f'--stream="port={self.config.port}"'
        # commands = [
        #     "webots",
        #     "--batch",
        #     "--no-sandbox",
        #     "--stderr",
        #     port_param,
        #     self.config.world_file,
        # ]
        commands = [
            "webots",
            "--batch",
            "--no-sandbox",
            "--stderr",
            '--stream="port=4000"',
            "/home/jelgar/Documents/uni/robotics/robo-gen/webots/worlds/labsheet_x.wbt",
        ]
        print("Running command {}".format(" ".join(commands)))
        self._webots = subprocess.Popen(commands)

        print("Opening webots")
        self.webots_pid = 0

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode="human"):
        pass


# env = WebotsEnv()

# commands = [
#     "webots",
#     "--batch",
#     "--no-sandbox",
#     "--stderr",
#     '--stream="port=4000"',
#     "/home/jelgar/Documents/uni/robotics/robo-gen/webots/worlds/labsheet_x.wbt",
# ]
#
# subprocess.Popen(commands)
env = gym.make("CartPole-v1")

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()

env.close()
