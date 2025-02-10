import gym
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class TradingEnv(gym.Env):
    """Reinforcement Learning Trading Environment"""
    def __init__(self, data):
        self.data = data
        self.current_step = 0
        self.balance = 10000
        self.position = 0

    def step(self, action):
        if action == 1:
            self.position = self.balance / self.data["Close"].iloc[self.current_step]
            self.balance = 0
        elif action == 2:
            self.balance = self.position * self.data["Close"].iloc[self.current_step]
            self.position = 0

        self.current_step += 1
        reward = self.balance + (self.position * self.data["Close"].iloc[self.current_step]) - 10000
        return np.array([self.balance, self.position]), reward, self.current_step >= len(self.data), {}

# Creating a simple Deep Q-Learning Model
def create_dqn():
    model = Sequential([
        Dense(24, input_dim=2, activation="relu"),
        Dense(24, activation="relu"),
        Dense(3, activation="linear")
    ])
    model.compile(loss="mse", optimizer=Adam(lr=0.001))
    return model
