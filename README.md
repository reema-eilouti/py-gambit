# Midterm-Project

test

### Team Members:
- Aseel Alzweri
- Hamzh Suilik
- Hisham Khalil
- Reema Eilouti
- Yahya Omari



**Chess Board**

    - Summary of idea.
    The chess board from our previous lab, but more enhanced, where you have more than two queens, you can have your horses/castles etc.

    - What problem or pain point does it solve?
    To visually know when my rocks are under attack and be prompted.

    - Minimum Viable Product (MVP) definition.
    A chess board, holding two teams rocks, you move both rocks, the program prompts you when you are under attack.



## User Stories

**Solo Mode**
1. As a player, I want solo play mode, so that I can play that game when no one is around
    - Feature Tasks:
        - Player can choose what color to play with.
        - Player can restart the game if wanted.
        - Player can choose the bot difficulty.
    - Acceptance Tests:
        - Ensure the color the player choose is correct.
        - Ensure the game is started when the player choose to restart the game.
        - Ensure the difficulty the player choose is correct.

**Multiplayer Mode**

2. As a player, I want multiplayer mode, so that I can play with others
    - Feature Tasks:
        - Players can choose to set a timer.
        - Players can choose to end the game with a draw or surrender.
    - Acceptance Tests:
        - Ensure the timer is working when players set it.
        - Ensure the game is ended when the players end the game.
       
**Available Moves**     

3. As a player, I want to see my available moves, so that I can move a piece of mine to attack directly a piece of other player pieces

    - Feature Tasks:
        - Player/s can require to highlight all pieces of his/her can move.
        - Player/s can require to see the highlighted pieces available moves. 
    - Acceptance Tests:
        - Ensure the highlighted pieces have correct moves and available for each player when they are required.
        - Ensure the available moves for the highlighted pieces are shown in the screen correctly.

**Under Attack**

4. As a player, I want to know what pieces of mine under attack, so that I can move the important piece of them and avoid a direct attack from the other player
    - Feature Tasks:
        - Player/s can require to highlight all pieces of his/her under attack
        - Player/s can require to see the highlighted pieces moves to escape
    - Acceptance Tests:
        - Ensure the highlighted pieces are under attack for each player when they are required
        - Ensure the escape moves for the highlighted pieces are shown in the screen correctly

**Chess Pieces**

5. As a player, I want to see chess pieces moves, so that I can remember what move I can do with a specific piece 
    - Feature Tasks:
        - Player/s can require to see the all pieces moves
    - Acceptance Tests:
        - Ensure the moves list has correct moves and is shown clear for players when it is required


## Wireframe

- Since we are building a game for the terminal without GUI or deployment on a website, this is the visual you'd expect for the user:
![wireframe](https://i.ibb.co/fN2DVJJ/chess-board.png)


## Domain Model
![domain_model](https://i.ibb.co/WDwDGhY/1.jpg)

- The first method called is init, inside the chess board is built and colored black and white.
    - init is called by creating an object of the ChessBoard class.
    - It does not return anything (None).

- The second method called is render, it is called by an object of the ChessBoard class, it will use matplotlib to draw the board and show it to the user.

- The add_red and add_blue methods are responsible to assign the chess pieces to the location provided by the user as input, it colors the square on the board and then calls the method render to update the view to the user.

- The main method holding most of the functionality to the user is the under_attack method. It calculates the coordinates of the pieces relating to each other and prompts the user when one of his/her pieces are being under possible attack by the other team.
    - This method is called after every call to add_red or add_blue.


## Database
- In our project, live – chess game, using database is not a basic requirement. However, we might set using a data base for storing players information/credentials,
 chess moves and final score as a stretch goal.
 -  For now, data will be stored in local variables in the code.

## Cooperation Plan

- **What are the key strengths of each person on the team?**
 
Aseel -> Good analytical skills and conceptual thinking.

Hamzh -> Good debugging skills.

Hisham -> Good planning skills and strategic thinking.

Reema -> Good organizational skills.

Yahya -> Good trouble shooting skills and positive energy.

- **How can you best utilize these strengths in the execution of your project?**

Having team members with good planning, strategic thinking and organizational skills will empower our team to have an efficient project plan especially in the early stages.
Also, having members with good analytical skills will help us define our problem domain and to visualize the parts of the solution beforehand, and to provide the best strategy to handle the problem.
Finally, having members in our team with good debugging and trouble shooting skills will help us solve errors/bugs in a timely manner and contribute to better optimize the solution.

 
- **In which professional competencies do you each want to develop greater strength?**

We have room to improve ourselves in time and task management also in decision making relating to choosing the most convenient algorithm and in our testing skills. 

- **Knowing that every person in your team needs to understand all aspects of the project, how do you plan to approach the day-to-day work?**

We plan on scheduling stand up meetings daily to divide the tasks and responsibilities for each team member, review previous work and also discuss any challenges we face.



## Conflict Plan

- **What will be your group’s process to resolve conflict, when it arises?**

Firstly after meeting in a zoom call were all team members are present we will look for the branch with the issue and compare the last commit with the current work and decide on which parts to keep and which to remove.

- **What will your team do if one person is taking over the project and not letting the other members contribute?**

We will have an internal meeting to discuss the matter in a diplomatic way ensuring the any misunderstandings are resolved with minimal damage. If we failed to solved internally, we'll probably ask the instructional team for advice. 

- **How will you approach each other and the challenges of the project knowing that it is impossible for all members to be at the exact same place in understanding and skill level?**

Communication is key when it comes to team work, we agreed on a strategy that ensures all team members are on the same page, by adding clear docstrings to each function and explaining it to the team by the responsible person.

- **How will you raise concerns to members who are not adequately contributing?**

During our daily meetings, we will make sure to communicate with members not contributing enough, and discuss possible working solution, as to overcome the issue.

- **How and when will you escalate the conflict if your resolution attempts are unsuccessful?**

If the conflict was not solved internally, we will escalate the conflict by reaching out the instructional team for help, support and advice.

## Communication Plan

- **What hours will you be available to communicate?***

The agreed on time availability is between 9:00 am - 5:00 pm. Extra working hours will be determined upon discussion according to each member availability.

- **What platforms will you use to communicate (ie. Slack, phone …)?**

We will be holding our meetings one Zoom, and we'll use Slack for quick updates and announcements.

- **How often will you take breaks?**

Breaks will be taken upon agreements, without a fixed schedule.

- **What is your plan if you start to fall behind?**

We will have a team meeting, where will re-prioritize the tasks according to their impact on the final outcome, and cooperate to meet the deadline.

- **How will you communicate after hours and on the weekend?**

Working during weekends and after hours will be upon every team member’s approval.

- **What is your strategy for ensuring everyone’s voice is heard?**

Every decision the team will make, will be based on voting.

- **How will you ensure that you are creating a safe environment where everyone feels comfortable speaking up?**

Every time a member has the right to share his thoughts, perspectives and ideas regarding any work done.

## Work Plan
- **How you will identify tasks, assign tasks, know when they are complete, and manage work in general?**

Based on the problem domain, time available, and strengths of each team member tasks will be identified and assigned. Progress and the task completion will be monitored using a project tool by the team leader, following the agreed on timeline.

- **What project management tool will be used?**

We will be using GitHub projects for managing the project, the team leader will be responsible for making sure that each feature task is being delivered on time.

## Git Process
- **What components of your project will live on GitHub?**

All project's file will be on GitHub, including the README file, the python files, Jupyter Notebooks.

- **How will you share the repository with your teammates?** 
- **How will you share the repository with your teammates? ** 


Each team member will be set as an owner of the repository. Such that branches will be created according to features.

- **What is your Git flow?**

Each feature will have it's own branch, pull request will be created after work is done. 

- **How many people must review a PR? Who merges PRs? How often will you merge? How will you communicate that it’s time to merge? Will you be using a PR review workflow? If so, consider:**

Pull Requests will be reviewed daily in a session, and the team leader will be responsible for merging the approved PRs at the end of that session. 


