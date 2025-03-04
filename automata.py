class Automata:

    # constructor to initialize an automata
    def __init__(self, states, alphabet, stateTransition, starting, accepting, input):
        self.state = states
        self.alphabet = alphabet
        self.stateTransition = stateTransition
        self.input = input
        self.starting = starting
        self.accepting = accepting
        self.current = starting
        self.inputIdx = 0


    # uses the dictionary of state transitions to go to the next state
    # when at end of input word, check if automata accepts input
    def nextState(self):

        self.current = self.stateTransition[(self.input[self.inputIdx], self.current)]
        self.inputIdx += 1

        if self.inputIdx == len(self.input):
            return self.current == self.accepting
        else:
            return None
    
    # iterates through state transition dict to find previous state based on current and prev input symbol
    def prevState(self):

        if self.inputIdx == 0:
            return
        
        self.inputIdx -= 1

        for (symbol, pState), cState in self.stateTransition.items():
            if cState == self.current and symbol == self.input[self.inputIdx]:
                self.current = pState
                break


    def acceptInput(self):
        for c in self.input:
            self.nextState()