# Sprint 1 Backlog

This document contains the issues that were selected for sprint 1.

### [Automata DSL](https://github.com/Holindauer/AutomataSim/issues/9)

- Assignee: Hunter
- Effort Estimate/Story Points: 7
- Acceptance Criteria:
     - The AutomatonDSL class will follow the factory design pattern for creating Automata class instances
    - The constructor should take in the states, start_state, accept_states, state_transition_func, and alphabet.
    - AutomataDSL should be capable of compiling arbitrary valid finite automata.
    - AutomataDSL should be capable of detecting invalid syntax and indicating failed instantiation.

### [Automata Simulation Class](https://github.com/users/Holindauer/projects/6/views/1?pane=issue&itemId=100018164&issue=Holindauer%7CAutomataSim%7C9)
- Assignee: Ziang
- Effort Estimate/Story Points: 7
- Acceptance Criteria:
    - Automata should be capable of simulating arbitrary valid finite automata.
    - Automata should be able to determine success or failure at a particular transition.
    - Automata should be able to progress forward/backward through states.

### [Database Backend:](https://github.com/users/Holindauer/projects/6/views/1?pane=issue&itemId=100018471&issue=Holindauer%7CAutomataSim%7C10)
- Assignee: Emmett
- Effort Estimate: 5
- Acceptance Criteria: 
    - Methods for the storage, retrieval, and verification of account details to/from the database. This includes both account creation and login.
    - Methods for storage and retrieval of automata.
    - Database schema involving two tables: USER and AUTOMATA as well as a script to instantiate it.

     - USER contains user credentials (primary key: user_name)
    - AUTOMATA contains formal automaton definitions (foreign key: user_name).

