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
        """parses full automaton definition from input file"""
        pass

    @staticmethod
    def _parse_components(automata_file: str):
        """
        Parses the name and five statements from the input file. If 5 statements are not 
        present, this will result in a syntax error. A tuple of the name and a list of
        the statements is returned.
        """

        # regex parses name and five statements
        automaton_header = r"\s*automaton\s+(?P<name>\w+)\s*"
        opening_brace = r"\s*\{"
        body = r"\s*(?P<stmt_1>.*?)\;\s*(?P<stmt_2>.*?)\;\s*(?P<stmt_3>.*?)\;\s*(?P<stmt_4>.*?)\;\s*(?P<stmt_5>.*?)\;\s*"
        closing_brace = r"\s*\}" 
        regex = f"{automaton_header}{opening_brace}{body}{closing_brace}"

        # parse name and body
        automaton_body = re.compile(regex, re.DOTALL)
        match = automaton_body.match(automata_file)

        # handle error for incorrect 
        if not match:
            return None, None

        # pattern match on the input file
        name = match.group("name")
        stmts = [match.group("stmt_" + str(i)) for i in range(1,6)]

        # remove whitespace
        rm_whitespace = lambda string: re.sub(r"\s+", "", string)
        stmts = [rm_whitespace(stmt) for stmt in stmts]

        return name, stmts

    @staticmethod 
    def parse_states(states: str):
        pass

    @staticmethod
    def parse_alphabet(alphabet: str):
        pass
        
    @staticmethod
    def parse_transition_func(transition_func: str):
        pass

    @staticmethod
    def parse_start_state(start_state: str):
        pass