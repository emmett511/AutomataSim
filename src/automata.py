class Automata:
    """Simulates a finite automaton. This class is intended
    to be created by the AutomatonDSL, which compiles formal
    descriptions of automata into Automata instances."""

    def __init__(self, states, alphabet, state_transition, starting, accepting, name=None):
        self.__states = states
        self.__alphabet = alphabet
        self.__state_transition = state_transition
        self.__starting = starting
        self.__accepting = accepting
        self.__current = starting
        self.__input_idx = 0
        self.__inputs_list = []
        self.__prevs = []
        self.__name = name

    def reset_to_beginning(self):
        """resets the automaton to start state"""
        self.__current = self.__starting
        self.__input_idx = 0
        self.__prevs = []

    def set_input(self, inputs_list):
        """set FA input string """
        for c in inputs_list:
            if c not in self.__alphabet:
                return False
            
        self.__inputs_list = inputs_list
        self.reset_to_beginning()
        return True

    def get_state(self):
        """returns current state of automata"""
        return self.__current

    def next_state(self):
        """    
        uses the dictionary of state transitions to go to the next state
        returns false if key is not in dictionary (automata does not accept input)
        when at end of input word, check if automata accepts input
        """
        if self.__input_idx >= len(self.__inputs_list):
            return None

        try:
            next_state = self.__state_transition[(self.__current, self.__inputs_list[self.__input_idx])]
            self.__prevs.append(self.__current)
            self.__current = next_state
            self.__input_idx += 1
        except KeyError:
            return False

        if self.__input_idx == len(self.__inputs_list):
            return self.__current in self.__accepting
        else: return None


    def prev_state(self):
        """finds the prev state by popping from the prevs list"""
        if self.__input_idx == 0:
            return
        
        self.__input_idx -= 1

        if self.__prevs:
            self.__current = self.__prevs.pop() 

    def run_till_complete(self):
        """runs automata to completion and returns if automata accepts the input string"""
        for _ in self.__inputs_list:
            is_accepted = self.next_state()
            if is_accepted is not None: return is_accepted
        
        return False
    
    def isAccepted(self):
        if self.__current in self.__accepting and self.__input_idx >= len(self.__inputs_list):
            return True
        else:
            return False
    
    def get_automata_data(self):
        """returns the data members of the automata"""
        return {
            "states": self.__states,
            "alphabet": self.__alphabet,
            "transition_func": self.__state_transition,
            "start_state": self.__starting,
            "accept_states": self.__accepting
        }

    def getIndex(self):
        return self.__input_idx

    def char_in_alphabet(self, char) -> bool:
        for c in char:
            if c not in self.__alphabet:
                return False
        return True

    def __repr__(self):
        return f"""
            Automata: {self.__name}\n
            states:\n
            {self.__states}\n
            alphabet:\n
            {self.__alphabet}\n
            state transition function:\n
            {self.__state_transition}\n
            start state:\n
            {self.__starting}\n
            accepting states:\n
            {self.__accepting}"""
    

def test_automata():
    states = {"q0", "q1", "q2", "q3"}
    alphabet = {'0', '1'}

    state_transition = {
        ("q0", '0') : "q1",
        ("q0", '1') : "q3",
        ("q1", '0') : "q1",
        ("q1", '1') : "q2",
        ("q2", '0') : "q3",
        ("q3", '1') : "q2"
    }

    starting_state = "q0"
    accept_states = {"q2"}

    return Automata(states, alphabet, state_transition, starting_state, accept_states)

