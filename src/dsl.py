import re

class AutomatonDSL:
    """
    AutomatonDSL is a compiler for a domain specific language that describes finite automata. 
    Below are the syntax rules of the language:
    
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
        
        # gather components
        (name, statements) = AutomatonDSL._parse_components(automata_file)
        if name is None or statements is None:
            return None

        # first parse states and alphabet (needed to ensure other components are valid)
        for statement in statements:
            if statement.startswith("states"):
                states = AutomatonDSL._parse_states(statement)
            if statement.startswith("alphabet"):
                alphabet = AutomatonDSL._parse_alphabet(statement)

        # then parse start state, accept states, and transition function
        for statement in statements:
            if statement.startswith("transition_func"):
                transition_func = AutomatonDSL._parse_transition_func(statement, states, alphabet)
            if statement.startswith("start_state"):
                start_state = AutomatonDSL._parse_start_state(statement, states)
            if statement.startswith("accept_states"):
                accept_states = AutomatonDSL._parse_accept_states(statement, states)

        # if any components are None, there was a syntax error somewhere
        if None in [states, alphabet, transition_func, start_state, accept_states]:
            return None
                
        # return automaton components as a dictionary
        return {
            "name": name,
            "states": states,
            "alphabet": alphabet,
            "transition_func": transition_func,
            "start_state": start_state,
            "accept_states": accept_states
        }

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
        automaton_body_regex = re.compile(regex, re.DOTALL)
        match = automaton_body_regex.match(automata_file)

        # incorrect syntax: automaton body rules not followed
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
    def _parse_states(states: str):
        """
        Parses states from whitespace stripped input string of form "states={<s1>,<s2>,...,<sn>}" 
        Returns a set of strings containing the state names or None if there is a syntax error.
        """
        
        # pattern match on the input string
        states_regex = re.compile(r"states=\{(?P<states>[\w+\s,]+)\}")
        match = states_regex.match(states)

        # incorrect syntax 
        if not match:
            return None
        
        # extract states into list
        parsed_states = match.group("states").split(",")

        # incorrect syntax: no duplicates in parsed states
        if len(parsed_states) != len(set(parsed_states)):
            return None
        
        return set(parsed_states)

    @staticmethod 
    def _parse_accept_states(accept_states: str, states: set):
        """
        Parses acceptstates from whitespace stripped input string of form "accept_states={<s1>,<s2>,...,<sn>}" 
        Returns a set of strings containing the state names or None if there is a syntax error.
        """
        
        # pattern match on the input string
        accept_states_regex = re.compile(r"accept_states=\{(?P<states>[\w+\s,]+)\}")
        match = accept_states_regex.match(accept_states)

        # incorrect syntax 
        if not match:
            return None
        
        # extract states into list
        parsed_states = match.group("states").split(",")

        # incorrect syntax: no duplicates in parsed states
        if len(parsed_states) != len(set(parsed_states)):
            return None
        
        # ensure that all accept states are in the set of states
        for state in parsed_states:
            if state not in states:
                return None

        return set(parsed_states)

    @staticmethod
    def _parse_alphabet(alphabet: str):
        """
        Parses alphabet from whitespace stripped input string of form "alphabet={<a1>,<a2>,...,<am>}"
        Returns a set of strings containing the alphabet symbols or None if there is a syntax error.
        """
        # pattern match on the input string
        alphabet_regex = re.compile(r"alphabet=\{(?P<symbols>[\w+\s,]+)\}")
        match = alphabet_regex.match(alphabet)

        # incorrect syntax 
        if not match:
            return None
        
        # extract symbols into list
        parsed_symbols = match.group("symbols").split(",")

        # incorrect syntax: ensure no duplicates in parsed symbols
        if len(parsed_symbols) != len(set(parsed_symbols)):
            return None
        
        # incorrect syntax: symbols should only be one char
        if any([len(s) != 1 for s in parsed_symbols]):
            return None

        return set(parsed_symbols)
        
    @staticmethod
    def _parse_transition_func(transition_func_str: str, states: set, alphabet: set):
        """
        Parses state transition function dictionary from whitespace stripped input string of form
        "transition_func = {(<s>, <a>): <s>, ..., (<s>, <a>): <s>};
        """

        # extract body of transition function
        body_regex = re.compile(r"transition_func=\{(?P<body>.*)\}")
        match = body_regex.match(transition_func_str)

        # incorrect syntax
        if not match:
            return None

        # extract each sub-element in order from body
        body_str = match.group("body")
        parentheses_removed = body_str.replace("(", "").replace(")", "") # remove parentheses
        transitions = re.split(r"[:,]", parentheses_removed)             # split on comma and colon

        # incorrect syntax: does not follow (<s>, <a>): <s> for every transition
        if 0 != len(transitions) % 3:
            return None

        # collect elements into dictionary 
        transition_func = {}
        for i in range(0, len(transitions), 3):
            transition_func[(transitions[i], transitions[i+1])] = transitions[i+2]

        # verify valid transition function
        for k, v in transition_func.items():

            # states in transition func inconsistent with previously defined states
            if k[0] not in states or v not in states:
                return None

            # symbols in transition func inconsistent with previously defined alphabet
            if k[1] not in alphabet:
                return None

        # ensure transition function is exhaustive by making sure
        # that for every state, there is a transition for each symbol
        for symbol in alphabet:
            for state in states:
                if (state, symbol) not in transition_func:
                    return None


        return transition_func

    @staticmethod
    def _parse_start_state(start_state: str, states: set):
        """
        Parses the start state from whitespace stripped input string of form "start_state=<s>"
        Returns the start state or None if there is a syntax error.
        """
        # pattern match on the input string
        start_state_regex = re.compile(r"start_state=(?P<state>\w+)")
        match = start_state_regex.match(start_state)
        
        # incorrect syntax
        if not match:
            return None

        # extract start state
        start = match.group("state")

        # incorrect syntax: start state must be an element of the automaton's states
        if start not in states:
            return None

        return start