import numpy as np

class MarkovChain:
    def __init__(self, states, transitions, initial_state, initial_distribution):
        self.states = states
        self.initial_state = initial_state
        self.initial_distribution = initial_distribution
        self.transitions = np.zeros((len(states), len(states)))

    def add_transition(self, state1, state2, poids):
        
        self.transitions[self.states.index(state1), self.states.index(state2)] = 0