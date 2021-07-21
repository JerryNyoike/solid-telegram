from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
import random
import numpy as np
import pandas as pd
from operator import lt, gt, le, ge
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


    def get_state(self, game, spaceship, enemies):
        ''' The state we store is whether:
            i) there is an enemy in front, to the left of or to the right of the agent
            ii) if the agent can move to the left and to the right.
            iii) if there are enemies within 5 points on the cordinates to the agents position.'''
        def enemy_in_position(postion, enemy):
            enemy_x , enemy_max_x = enemy.coords()
            if position == "front":
                op_1, op_2 = le, ge
            elif position == "left":
                op_1, op_2 = gt, gt
            else:
                op_1, op_2 = lt, lt

            return op_1(spaceship.x, enemy_x) and op_2(spaceship.x, enemy_max_x)

        enemy_left = partial(enemy_in_position, "left")

        enemy_right = partial(enemy_in_position, "right")

        enemy_top = partial(enemy_in_position, "front")

        def move_in_direction(direction):
            ''' Checks if the agent has reached the left border of the screen. '''
            if direction == "left":
                return spaceship.x > 20
            return spaceship.x < width - 20

        state = [
                move_in_direction("left"),
                move_in_direction("right"),
                len(list(filter(enemy_left, enemies))) != 0,
                len(list(filter(enemy_right, enemies))) != 0,
                len(list(filter(enemy_front, enemies))) != 0,
                ]

        return state


    def set_reward(self, player, hit, lost):
        self.reward = 0
        if hit:
            self.reward = 10
            return self.reward
        else:
            self.reward = -10
            return self.reward

        if lost:
            self.reward = -5

        return self.reward
        


    def remember(self, state, action, reward, next_state, done):
        pass


    def replay_new(self, memory, batch_size):
        pass


    def train_short_memory(self, state, action, reward, next_state, done):
        pass
