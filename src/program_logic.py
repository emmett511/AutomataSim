from dsl import AutomatonDSL

class ProgramLogic:
    def __init__(self):
        self.current_automata = None

    def compile_automata(self, automaton_def: str):
        """compiles an automata from description written in automaton dsl. 
        Delegates compilation to the automaton dsl compiler."""
        automaton = AutomatonDSL.parse_automaton(automaton_def)
        if automaton:
            self.current_automata = automaton
        else:
            self.current_automata = "SYNTAX ERROR:" + "\n\n" + automaton_def
