from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
import random
import numpy as np
import pandas as pd
from operator import add
import collections


class DQNAgent(object):
    def __init__(self, params):
        self.reward = 0
        self.gamma = 0.9
        self.dataframe = pd.DataFrame()
        self.short_memory = np.array()
        self.agent_target = 1
        self.agent_predict = 0
        self.learning_rate
        self.epsilon = 1
        self.actual = []
        self.first_layer = params['first_layer_size']
        self.second_layer = params['second_layer_size']
        self.third_layer = params['third_layer_size']
        self.memory = collections.deque(maxlen=params['memory_size'])
        self.weights = params['weights_path']
        self.load_weights = params['load_weights']
        self.model = self.network()


    def network(self):
        model = Sequential()
        model.add(Dense(output_dim=self.first_layer, activation='relu', input_dim=11))
        model.add(Dense(output_dim=self.second_layer, activation='relu'))
        model.add(Dense(output_dim=self.third_layer, activation='relu'))
        model.add(Dense(output_dim=3, activation='softmax'))
        opt = Adam(self.learning_rate)

        model.compile(loss='mse', optimizer=opt)

        if self.load_weights:
            model.load_weights(self.weights)

        return model


    def get_state(self, game, player, enemy):
        pass


    def set_reward(self, player, crash):
        pass


    def remember(self, state, action, reward, next_state, done):
        pass


    def replay_new(self, memory, batch_size):
        pass


    def train_short_memory(self, state, action, reward, next_state, done):
        pass
