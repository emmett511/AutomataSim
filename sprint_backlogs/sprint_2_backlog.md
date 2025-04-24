# Sprint 2 Backlog

This document contains the issues that were selected for sprint 2.

### [Input String for Compiled Automata](https://github.com/users/Holindauer/projects/6/views/1?filterQuery=assignee%3AHolindauer&pane=issue&itemId=100017514)
- Assignee: Hunter
- Effort Estimate/Story Points: 7
- Acceptance Criteria:
    - The user can input a string of characters, accept string with valid characters, and reject strings with invalid characters.
    - Runs an input of characters on an automata and switches to correct states.

### [Automata Simulation Class](https://github.com/Holindauer/AutomataSim/commit/7667b07c9e655ccd1bb043d06072cd944f11d0d1)
- Assignee: Hunter, Ziang
- Effort Estimate/Story Points: 7
- Acceptance Criteria:
    - Users can simulate input strings on automata and can progress through states.
    - Use right and left arrows to move back and forth between states.
    - Displays error for invalid input and runs correctly on valid input.

### [Automata Visualization](https://github.com/users/Holindauer/projects/6/views/1?pane=issue&itemId=100018518)
- Assignee: Ziang
- Effort Estimate/Story Points: 7
- Acceptance Criteria:
    - Extend the Automata class to visualize finite automata using Graphviz.
    - Visualize transitions based on input and allow stepping forward/backward through states.

### [Account Creation](https://github.com/Holindauer/AutomataSim/issues/4)
- Assignee: Emmett
- Effort Estimate: 7
- Acceptance Criteria: 
    - Allows users to create an account with a valid username and password.
    - Displays appropriate success or error messages.
    - Stores account details in the database and navigates to the login page on success.

### [Login](https://github.com/Holindauer/AutomataSim/issues/2)
- Assignee: Emmett
- Effort Estimate: 7
- Acceptance Criteria: 
    - Allows users to log in with a valid username and password.
    - Displays errors for incorrect username or password.
    - Navigates to the main application page on successful login.
    - Retrieves credentials from the database for verification.

### [Home Page](https://github.com/Holindauer/AutomataSim/issues/1)
- Assignee: Emmett
- Effort Estimate: 7
- Acceptance Criteria: 
    - Displays buttons to create an account, log in, or exit the application.
    - Navigates to the appropriate page based on the user’s selection.
    - Exits the program when the exit button is clicked.