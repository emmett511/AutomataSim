import pytest
from dsl import AutomatonDSL

def setup_correct_automaton():
    """Correct Automata Description"""
    return """
    automaton hector {
        states = {q0, q1};
        alphabet = {0, 1};
        transition_func = {
            (q0, 0): q1,
            (q0, 1): q0,
            (q1, 0): q0,
            (q1, 1): q1
        };
        start_state = q0;
        accept_states = {q1};
    }
    """

def setup_automaton_missing_components():
    """Automata Description that is missing states component"""
    return """
    automaton hector {
        alphabet = {0, 1};
        transition_func = {
            (q0, 0): q1,
            (q0, 1): q0,
            (q1, 0): q0,
            (q1, 1): q1
        };
        start_state = q0;
        accept_states = {q1};
    }
    """

def test_parse_components():
    """Tests that components of properly formatted automaton are parsed correctly"""
    # parse correct automaton
    automaton_file = setup_correct_automaton()
    name, body = AutomatonDSL._parse_components(automaton_file)
    print(body)
    # ensure all components are presetn
    assert name == "hector"
    assert 'states={q0,q1}' in body
    assert 'alphabet={0,1}' in body
    assert 'transition_func={(q0,0):q1,(q0,1):q0,(q1,0):q0,(q1,1):q1}' in body
    assert 'start_state=q0' in body
    assert 'accept_states={q1}' in body

def test_parse_missing_component_fails():
    """Tests that components of properly formatted automaton are parsed correctly"""
    # parse correct automaton
    automaton_file = setup_automaton_missing_components()
    name, body = AutomatonDSL._parse_components(automaton_file)
    # ensure this does not compile
    assert name is None
    assert body is None

def setup_correct_states_component():
    return "states={q0,q1,q3,q4}"

def setup_states_component_with_duplicates():
    return "states={q0,q1,q3,q4,q0}"

def setup_states_missing_braces_component():
    return "states={q0 q1,q3,q4"

def test_parse_states():
    """tests that correct syntax is correctly parsed"""
    states_str = setup_correct_states_component()
    assert AutomatonDSL._parse_states(states_str) == {'q0', 'q1', 'q3', 'q4'}

def test_parse_states_with_missing_braces():
    """tests that incorrect syntax is caught as syntax error"""
    states_str = setup_states_missing_braces_component()
    assert AutomatonDSL._parse_states(states_str) is None

def test_parse_states_with_duplicates():
    """tests that duplicate states are caught as syntax error"""
    states_str = setup_states_component_with_duplicates()
    assert AutomatonDSL._parse_states(states_str) is None

def setup_correct_alphabet_component():
    return "alphabet={0,1}"

def setup_alphabet_component_with_duplicates():
    return "alphabet={0,1,0}"

def setup_alphabet_missing_braces_component():
    return "alphabet={0,1"

def setup_alphabet_invalid_symbols():
    """Symbols should only be single char"""
    return "alphabet={0,10}"

def test_parse_alphabet():
    """tests that correct alphabet syntax is correctly parsed"""
    alphabet_str = setup_correct_alphabet_component()
    assert AutomatonDSL._parse_alphabet(alphabet_str) == {'0', '1'}

def test_duplicates():
    """tests that duplicate symbols are caught as syntax error"""
    alphabet_str = setup_alphabet_component_with_duplicates()
    assert AutomatonDSL._parse_alphabet(alphabet_str) is None

def test_missing_braces():
    """tests that missing braces are caught as syntax error"""
    alphabet_str = setup_alphabet_missing_braces_component()
    assert AutomatonDSL._parse_alphabet(alphabet_str) is None

def setup_correct_start_state():
    return "start_state=q0"

def setup_incorrect_start_state():
    return "start_state=state9"

def test_correct_start_state():
    """tests that start state parsing is correct (checks that start states is in states set)"""
    states_str = setup_correct_states_component()
    start_state_str = setup_correct_start_state()
    assert AutomatonDSL._parse_start_state(start_state_str, states_str) == 'q0'

def test_incorrect_start_state():
    """tests that incorrect start state is caught as syntax error"""
    states_str = setup_correct_states_component()
    start_state_str = setup_incorrect_start_state()
    assert AutomatonDSL._parse_start_state(start_state_str, states_str) is None