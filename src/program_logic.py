from dsl import AutomatonDSL

class ProgramLogic:
    def __init__(self):
        self.current_automata = None
        self.valid_automata = False
        self.valid_input_string = False

    def compile_automata(self, automaton_def: str):
        """compiles an automata from description written in automaton dsl. 
        Delegates compilation to the automaton dsl compiler."""
        automaton = AutomatonDSL.parse_automaton(automaton_def)
        if automaton:
            self.current_automata = automaton
            self.valid_automata = True
            self.valid_input_string = False # reset on new automaton
        else:
            self.current_automata = "Automata definition: \n\nSYNTAX ERROR:\n\n" + automaton_def
            self.valid_automata = False

    def set_input_string(self, input_string: str):
        if self.current_automata.char_in_alphabet(input_string):
            self.valid_input_string = True
            self.input_string = input_string
        else:
            self.valid_input_string = False
            self.input_string = "SYNTAX ERROR:" + "\n\n" + input_string