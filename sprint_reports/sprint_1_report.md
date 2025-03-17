
# Sprint 1 Report
Video Link: TODO: update link

## What's New (User Facing)

- Finite automata compilation from domain specific language.
- Database management for:
    - User account creation
    - User credentials validation
    - Saving for user automaton
    - Retrieval for user automaton

* Implemented class for a domain specific language that compiles formal descriptions of finite automata into simulations.
* Implemented class for automata simulations. Simulates finite automata on input strings. The DSL class is considered a factory class for Automata.
* Implemented a class to manage the DBMS. This class is currently able to 


## Work Summary (Developer Facing)

In this sprint, we focused primarily on the backend, targeting automaton simulation and database management. 

With respect to simulation, we implemented a factory class (AutomatonDSL) that is a minimal domain specific language compiler that takes formal descriptions of finite automata, and compiles them into working simulations. These simulations are the Automata class, which are able to simulate finite state machines on input strings. 

On the database front, we implemented the functionality require to create and log in to accounts. As well as save the aforementioned Automata to a local database.

By focusing on the backend, we have implemented a majority of the functional requirements of the project, leaving incorporation into the UI as our next steps.

## Unfinished Work

In this sprint, we accomplished all major backend functionality we intended to implemented. 

The only thing we did not accomplish was incorporation of these backend features into the UI, but this was not the intention for this sprint. We intentionally implemented the backend first so that it would be more straightforward to implement the front end.

## Completed Issues/User Stories

Here are links to the issues that we completed in this sprint:
* [DSL issue](https://github.com/Holindauer/AutomataSim/issues/3)
* [Database backend issue](https://github.com/Holindauer/AutomataSim/issues/10)
* [Automata class issue](https://github.com/Holindauer/AutomataSim/issues/9)


## Incomplete Issues/User Stories

We accomplished all Issues/User stories we intended to accomplish.

## Code Files for Review

Please review the following code files, which were actively developed during this
sprint, for quality:

- [DSL](https://github.com/Holindauer/AutomataSim/blob/main/src/dsl.py)
- [DSL tests](https://github.com/Holindauer/AutomataSim/blob/main/src/test_dsl.py)
- [Automta](https://github.com/Holindauer/AutomataSim/blob/main/src/automata.py)
- [Automata tests](https://github.com/Holindauer/AutomataSim/blob/main/src/test_automata.py)
- [Database](https://github.com/Holindauer/AutomataSim/blob/main/src/database.py)
- [Databas Initialization](https://github.com/Holindauer/AutomataSim/blob/main/src/db_setup.py)
- [Databse tests](https://github.com/Holindauer/AutomataSim/blob/main/src/test_database.py)

## Retrospective Summary
Here's what went well:
* Assigning seperate tasks to each team member in isolation meant we could work asynchronously on our components.
* We efficient implement all of our intentions.

Here's what we'd like to improve:
* Next time we would like to improve the kanban board organization for our sprint. We used it somewhat informally and did not document till the end.

Here are changes we plan to implement in the next sprint:
* Update kanban board more frequently throughout the sprint to better inform teamates about project status.