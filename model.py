from ast import List
from operator import truediv
import random



class MDP:
    def __init__(self):
        self.states = None
        self.actions = None
        self.initial_state = None
        self.initial_distribution = None
        self.transitions = {}

    def set_initial_state(self, initial_state):
        self.initial_state = initial_state

    def set_initial_distribution(self, initial_distribution):
        self.initial_distribution = initial_distribution

        
    def set_states(self, states):
        self.states = states
        self.initial_state = states[0]

    def set_actions(self, actions):
        self.actions = actions
        

    def add_transition(self, state1:str, states:List, weights:List, action:str):
        """Add a transition using a defined action from a source state to a set of states"""
        existing_actions = self.transitions.get(state1,{}).keys()
        # check if the new action violates any rule
        if action != 'N' and 'N' in existing_actions:
            raise ValueError(f'States without actions cannot receive an action {list(existing_actions)} != {action}')
        elif action == 'N' and 'N' not in existing_actions and len(existing_actions)>0:
            raise ValueError(f'States with defined actions cannot have a transition without actions {list(existing_actions)} != {action}')
        # if not we can add the action and its transitions
        else:
            final_transitions = {}
            for state,weight in zip(states,weights):
                final_transitions[state] = weight
            existing = self.transitions.get(state1,{}).get(action,{})
            final_transitions = existing | final_transitions
            self.transitions[state1] = self.transitions.get(state1,{}) | {action:final_transitions}

    def simulate_state(self,state_tree:dict,):
        """Simulates a transition using a defined action and evaluating a probability in the prefered action"""
        if not state_tree:
            return None
        total_weight = sum(list(state_tree.values()))
        choice = random.random() * total_weight
        acc = 0
        for state,weight in state_tree.items():
            acc += weight
            if choice < acc:
                return state
    
    def choose_action(self,state_tree,state):
        current_state = None
        if 'N' in state_tree.keys():
            print(f'State: {state} simulating with no action.\n')
            current_state = self.simulate_state(state_tree['N'])
        else: 
            action = input(f'State {state}, please select an action: {list(state_tree.keys())}\n')
            current_state = self.simulate_state(state_tree.get(action,{}))
        return current_state

    def continue_simulation(self,simulated):
        decision = input(f'Simulated states are: {simulated}. Do you whish to continue? Y/N\n')
        if decision.capitalize() == 'Y':
            return True
        return False
        

    def simulate(self):
        if not self.initial_state: 
            raise ValueError('No initial state detected, please review your mdp definition')
        continue_sim = True
        print(f'Starting simulation, Initial state: {self.initial_state}')
        simulated_states = [self.initial_state]
        state_tree = self.transitions.get(self.initial_state,{})
        current_state = self.initial_state
        
        while continue_sim and state_tree:
            current_state = self.choose_action(state_tree,current_state)
            if not current_state:
                break
            simulated_states.append(current_state)
            state_tree = self.transitions.get(current_state,{})
            continue_sim = self.continue_simulation(simulated_states)
            
            
        return simulated_states
                

                



                





    def __str__(self):
        return f"States: {self.states}\nActions: {self.actions}\nInitial State: {self.initial_state}\nInitial Distribution: {self.initial_distribution}\nTransitions: \n"
