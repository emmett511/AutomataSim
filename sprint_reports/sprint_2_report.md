
# Sprint 1 Report
Video Link: TODO: update link

## What's New (User Facing)

- Login and Account Creation page
- Simulation page including:
    - Inputting automata
    - Inputting string for automata
    - Visualization of automata and stepping through states

* Implemented classes for homepage, login and account creation features
* Implemented class for simulation page, which allows users to input automatas and simulate them
* Implemented Visualization function in program logic, which visualizes current state of automata as PNG
* Implemented controller class for pages

## Work Summary (Developer Facing)

In this sprint we focused mainly on creating the UI, as our major backend components were done in the previous sprint. 

We implemented a login page and home page class which allows the user to create accounts and log in to those accounts.

For simulating the automata. We implemented the simulation page. It allows the user to input automatas and input strings. The input automata is parsed by the DSL. Then it is displayed using the visualize function. 

To visualize the automata, we implemented a function to render the current state of the automata as an image. The image is displayed on the simulation page. When previous/next state is clicked a new image is rendered and displayed.

We completed most of our functional requirements for the project in this sprint.

## Unfinished Work

In this sprint we completed most of our functional requirements.

We were not able to complete the save and load automata features. Which will allow users to save automatas to their account and load them. We also were not able to complete some non functional requirements. For example dynamically scaling the UI to work better on differently sized screens.

## Completed Issues/User Stories

Here are links to the issues that we completed in this sprint:
* [Simulation page](https://github.com/Holindauer/AutomataSim/issues/6)
* [Input on Simulation Page](https://github.com/Holindauer/AutomataSim/issues/5)
* [Visualize Automata](https://github.com/Holindauer/AutomataSim/issues/11)
* [Login Page](https://github.com/Holindauer/AutomataSim/issues/2)
* [Account Creation](https://github.com/Holindauer/AutomataSim/issues/4)
* [Home Page](https://github.com/Holindauer/AutomataSim/issues/1)



## Incomplete Issues/User Stories

We accomplished all Issues/User stories we intended to accomplish.

## Code Files for Review

Please review the following code files, which were actively developed during this
sprint, for quality:
- [Simulation page](https://github.com/Holindauer/AutomataSim/blob/main/src/simulation_page.py)
- [Visualize Automata](https://github.com/Holindauer/AutomataSim/blob/main/src/program_logic.py)
- [Login Page](https://github.com/Holindauer/AutomataSim/blob/main/src/login_page.py)
- [Account Creation](https://github.com/Holindauer/AutomataSim/blob/main/src/create_account_page.py)
- [Home Page](https://github.com/Holindauer/AutomataSim/blob/main/src/home_page.py)
- [Page Control](https://github.com/Holindauer/AutomataSim/blob/main/src/page_control.py)



## Retrospective Summary
Here's what went well:
* We assigned seperate tasks to each team member, working in isolation on our components
* We were able to integrate our seperate components of the UI without any major issues
* All team memebers were able to complete their tasks for this sprint.


Here's what we'd like to improve:
* We think the work we did in this sprint was well executed, for the next sprint we would like to be faster with doing high quality work.

Here are changes we plan to implement in the next sprint:
* We will be more proactive in the next sprint