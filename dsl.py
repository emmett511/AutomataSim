import re

class AutomatonDSL:
    """
    AutomatonDSL is a compiler for a domain specific language that describes finite automata. 
    
    The following syntax rules apply:
    
    The following keywords are reserved: 
        - automaton
        - states
        - alphabet
        - transition_func
        - start_state
        - accept_states

    - Only one automaton can be defined per file.
    - Each statement is seperated by a semicolon. 
    - Elements of the <alphabet> are restricted to single characters.
    - All elements in <accept_states> and <start_state> must be elements of <states>.
    - The <transition_func> must exhaustively define the transition of every state 
      for every symbol in the alphabet.
    

    Full syntax of a valid automaton definition:

    automaton <name> {

        states = {<s1>, <s2>, ..., <sn>};
    
        alphabet = {<a1>, <a2>, ..., <am>};
    
        transition_func = {
            (<s>, <a>): <s>,
            ...
            (<s>, <a>): <s>
            };

        start_state = <s>;

        accept_states = {<s>, <s>, ..., <s>};
    }
    """
    @staticmethod
    def parse_automaton(automata_file: str):
        pass

        