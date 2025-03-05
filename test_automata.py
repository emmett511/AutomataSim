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


def test_setInput(testAutomata):        # tests setInput on cases where input words are valid and invalid
    assert testAutomata.setInput(['0','0','1','0','1']) == True         
    assert testAutomata.setInput(['1','0','2','0','1']) == False


def test_validNextState(testAutomata):       # testing nextState when input is accepted
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


def test_invalidNextState(testAutomata):        # testing nextState when input is not accepted
    testAutomata.setInput(['0','1','0'])
    assert testAutomata.getState() == "q0"
    testAutomata.nextState()
    assert testAutomata.getState() == "q1"
    testAutomata.nextState()
    assert testAutomata.getState() == "q2"
    assert testAutomata.nextState() == False
    assert testAutomata.getState() == "q3"


def test_runTillComplete(testAutomata):         # testing run to completion when input is accepted
    testAutomata.setInput(['0','0','1','0','1'])
    assert testAutomata.runTillComplete() == True


def test_runTillComplete(testAutomata):         # testing run to completion when input is not accepted
    testAutomata.setInput(['0','1','1'])
    assert testAutomata.runTillComplete() == False


def test_resetToBeginning(testAutomata):           # test resetToBeginning
    testAutomata.setInput(['0','0','1','0','1']) 
    testAutomata.runTillComplete()
    testAutomata.resetToBeginning()
    assert testAutomata.getState() == "q0"


def test_prevState(testAutomata):            # test prevState
    testAutomata.setInput(['0', '0', '1'])
    testAutomata.runTillComplete()
    assert testAutomata.getState() == "q2"
    testAutomata.prevState()
    assert testAutomata.getState() == "q1"
    testAutomata.prevState()
    assert testAutomata.getState() == "q1"
    testAutomata.prevState()
    assert testAutomata.getState() == "q0"


def test_emptyPrevState(testAutomata):           # test prevState when input is empty
    testAutomata.prevState()
    assert testAutomata.getState() == "q0"

