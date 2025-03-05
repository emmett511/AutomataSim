import pytest
from automata import Automata

@pytest.fixture
def testAutomata():
    states = {"q0", "q1", "q2", "q3"}

    alphabet = {'0', '1'}

    stateTransition = {
        ('0', "q0") : "q1",
        ('1', "q0") : "q3",
        ('0', "q1") : "q1",
        ('1', "q1") : "q2",
        ('0', "q2") : "q3",
        ('1', "q3") : "q2"
    }

    startingState = "q0"

    acceptStates = {"q2"}


    return Automata(states, alphabet, stateTransition, startingState, acceptStates)


def test_setInput(testAutomata):
    assert testAutomata.setInput(['0','0','1','0','1']) == True
    assert testAutomata.setInput(['1','0','2','0','1']) == False


def test_nextState(testAutomata):

    # testing nextState when input is accepted
    testAutomata.setInput(['0','0','1','0','1'])
    assert testAutomata.getState() == "q0"
    testAutomata.nextState()
    assert testAutomata.getState() == "q1"
    testAutomata.nextState()
    assert testAutomata.getState() == "q1"
    testAutomata.nextState()
    assert testAutomata.getState() == "q2"
    testAutomata.nextState()
    assert testAutomata.getState() == "q3"
    assert testAutomata.nextState() == True
    assert testAutomata.getState() == "q2"
    
    # testing nextState when input is not accepted
    testAutomata.setInput(['0','1','0'])
    assert testAutomata.getState() == "q0"
    testAutomata.nextState()
    assert testAutomata.getState() == "q1"
    testAutomata.nextState()
    assert testAutomata.getState() == "q2"
    assert testAutomata.nextState() == False
    assert testAutomata.getState() == "q3"



def test_runTillComplete(testAutomata):

    # testing run to completion when input is accepted
    testAutomata.setInput(['0','0','1','0','1'])
    assert testAutomata.runTillComplete() == True

    # testing on when input is not accepted
    testAutomata.setInput(['0','1','1'])
    assert testAutomata.runTillComplete() == False

