

class Automata:

    # constructor to initialize an automata
    def __init__(self, states, alphabet, stateTransition, starting, accepting):
        self.__states = states
        self.__alphabet = alphabet
        self.__stateTransition = stateTransition
        self.__starting = starting
        self.__accepting = accepting
        self.__current = starting
        self.__inputIdx = 0
        self.__inputsList = []
        self.__prevs = []


    # resets the automata
    def resetToBeginning(self):
        self.__current = self.__starting
        self.__inputIdx = 0
        self.__prevs = []


    # input string for automata to run
    def setInput(self, inputsList):

        for c in inputsList:
            if c not in self.__alphabet:
                return False
            
        self.__inputsList = inputsList
        self.resetToBeginning()
        return True


    # returns current state of automata
    def getState(self):
        return self.__current


    # uses the dictionary of state transitions to go to the next state
    # returns false if key is not in dictionary (automata does not accept input)
    # when at end of input word, check if automata accepts input
    def nextState(self):

        if self.__inputIdx >= len(self.__inputsList):
            return None

        try:
            next_state = self.__stateTransition[(self.__inputsList[self.__inputIdx], self.__current)]
            self.__prevs.append(self.__current)
            self.__current = next_state
            self.__inputIdx += 1
        except KeyError:
            return False

        if self.__inputIdx == len(self.__inputsList):
            return self.__current in self.__accepting
        else: return None


    # finds the previous by popping from the prevs list
    def prevState(self):

        if self.__inputIdx == 0:
            return
        
        self.__inputIdx -= 1

        if self.__prevs:
            self.__current = self.__prevs.pop() 


    # runs automata to completion and returns if automata accepts the input string
    def runTillComplete(self):

        for _ in self.__inputsList:
            isAccepted = self.nextState()
            if isAccepted is not None: return isAccepted
        
        return False
    

    # returns the data members of the automata
    def getAutomataData(self):
        return {
            "states": self.__states,
            "alphabet": self.__alphabet,
            "transition_func": self.__stateTransition,
            "start_state": self.__starting,
            "accept_states": self.__accepting
        }