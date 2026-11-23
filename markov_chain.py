class MarkovChain:
    def __init__(self):
        self.states = None
        self.actions = None
        self.initial_state = None
        self.initial_distribution = None
        self.transitions_no_act = None
        self.transitions_act = None

    def set_initial_state(self, initial_state):
        self.initial_state = initial_state

    def set_initial_distribution(self, initial_distribution):
        self.initial_distribution = initial_distribution

        
    def set_states(self, states):
        self.states = states
        self.initial_state = states[0]
        self.transitions_act = [[None for _ in range(len(states)) ]  for _ in range(len(states))]
        self.transitions_no_act = [[0] for _ in range(len(states)) for _ in range(len(states))]

    def set_actions(self, actions):
        self.actions = actions
        

    def add_transition_act(self, state1, state2, poids, action):
        insertCell = self.transitions[self.states.index(state1)][self.states.index(state2)]
        if insertCell == None:
            self.transitions_act[self.states.index(state1)][self.states.index(state2)] = {action:poids}
        elif type(insertCell) == dict:
            self.transitions_act[self.states.index(state1)][self.states.index(state2)][action] = poids

    def add_transition_no_act(self,state1,state2,poids):
        self.transitions_no_act[self.states.index(state1)][self.states.index(state2)] = poids

    def show_transitions(self):
        s = "    "
        for k in range(len(self.states)):
            s+= f"{self.states[k]} "
        s+= "\n"
        for i in range(len(self.states)):
            s+= f"{self.states[i]}"
            for j in range(len(self.states)):
                s += f" {self.transitions[i][j]} "
            s+= "\n"
        return s



    def __str__(self):
        return f"States: {self.states}\nActions: {self.actions}\nInitial State: {self.initial_state}\nInitial Distribution: {self.initial_distribution}\nTransitions: \n{self.show_transitions()}"
