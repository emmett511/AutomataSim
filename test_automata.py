import pytest
from automata import Automata

@pytest.fixture
def test_automata():
    states = {"q0", "q1", "q2", "q3"}
    alphabet = {'0', '1'}

    state_transition = {
        ('0', "q0") : "q1",
        ('1', "q0") : "q3",
        ('0', "q1") : "q1",
        ('1', "q1") : "q2",
        ('0', "q2") : "q3",
        ('1', "q3") : "q2"
    }

    starting_state = "q0"
    accept_states = {"q2"}

    return Automata(states, alphabet, state_transition, starting_state, accept_states)

def test_set_input(test_automata):        
    """tests setInput on cases where input words are valid and invalid"""
    assert test_automata.set_input(['0','0','1','0','1']) == True         
    assert test_automata.set_input(['1','0','2','0','1']) == False

def test_valid_next_state(test_automata):       
    """testing nextState when input is accepted"""
    test_automata.set_input(['0','0','1','0','1'])
    assert test_automata.get_state() == "q0"
    test_automata.next_state()
    assert test_automata.get_state() == "q1"
    test_automata.next_state()
    assert test_automata.get_state() == "q1"
    test_automata.next_state()
    assert test_automata.get_state() == "q2"
    test_automata.next_state()
    assert test_automata.get_state() == "q3"
    assert test_automata.next_state() == True
    assert test_automata.get_state() == "q2"


def test_invalid_next_state(test_automata):        
    """testing nextState when input is not accepted"""
    test_automata.set_input(['0','1','0'])
    assert test_automata.get_state() == "q0"
    test_automata.next_state()
    assert test_automata.get_state() == "q1"
    test_automata.next_state()
    assert test_automata.get_state() == "q2"
    assert test_automata.next_state() == False
    assert test_automata.get_state() == "q3"

def test_run_till_complete_accepted(test_automata):        
    """testing run to completion when input is accepted"""
    test_automata.set_input(['0','0','1','0','1'])
    assert test_automata.run_till_complete() == True

def test_run_till_complete_not_accepted(test_automata):        
    """testing run to completion when input is not accepted"""
    test_automata.set_input(['0','1','1'])
    assert test_automata.run_till_complete() == False

def test_reset_to_beginning(test_automata):          
    """testing resetToBeginning"""
    test_automata.set_input(['0','0','1','0','1']) 
    test_automata.run_till_complete()
    test_automata.reset_to_beginning()
    assert test_automata.get_state() == "q0"

def test_prev_state(test_automata):           
    """testing prevState"""
    test_automata.set_input(['0', '0', '1'])
    test_automata.run_till_complete()
    assert test_automata.get_state() == "q2"
    test_automata.prev_state()
    assert test_automata.get_state() == "q1"
    test_automata.prev_state()
    assert test_automata.get_state() == "q1"
    test_automata.prev_state()
    assert test_automata.get_state() == "q0"

def test_empty_prev_state(test_automata):          
    """testing prevState when input is empty"""
    test_automata.prev_state()
    assert test_automata.get_state() == "q0"

