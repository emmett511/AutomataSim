

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

    # input string for automata to run
    def setInput(self, inputsList):

        for c in inputsList:
            if c not in self.__alphabet:
                return False
            
        self.__inputsList = inputsList
        return True

    # returns current state of automata
    def getState(self):
        return self.__current


    # resets the automata
    def resetToBeginning(self):
        self.__current = self.__starting
        self.__inputIdx = 0


    # uses the dictionary of state transitions to go to the next state
    # when at end of input word, check if automata accepts input
    def nextState(self):

        self.__current = self.__stateTransition[(self.__inputsList[self.__inputIdx], self.__current)]
        self.__inputIdx += 1

        if self.__inputIdx == len(self.__inputsList):
            return self.__current in self.__accepting
        else:
            return None
    

    # iterates through state transition dict to find previous state based on current and prev input symbol
    def prevState(self):

        if self.__inputIdx == 0:
            return
        
        self.__inputIdx -= 1

        for (symbol, pState), cState in self.__stateTransition.items():
            if cState == self.__current and symbol == self.__inputsList[self.__inputIdx]:
                self.__current = pState
                break

    # runs automata to completion and returns if automata accepts the input string
    def runTillComplete(self):
        isAccepted = None

        for c in self.__inputsList:
            isAccepted = self.nextState()
        
        return isAccepted
    
    # returns the data members of the automata
    def getAutomataData(self):
        return {
            "states": self.__states,
            "alphabet": self.__alphabet,
            "transition_func": self.__stateTransition,
            "start_state": self.__starting,
            "accept_states": self.__accepting
        }