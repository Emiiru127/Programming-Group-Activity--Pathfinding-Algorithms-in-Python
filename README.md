Group Name: Teletubbies 

Members: 

Austria, Nelson

Baway, Arcelie

Canceran, Emil 

Catalan, Hans 

De Jose, James 

Diarios, Vaneza

Elago, Arniño 

Marasigan, John Aron 

Roa, Cristine Joy



2.1) Overview of the algorithms implemented.

Greedy Best-First Search (GBFS):

GBFS finds the shortest path to a goal node using a heuristic that estimates the distance from the current node to the goal. Uses a priority queue to explore nodes based solely on their heuristic values. It expands the most promising node without considering the cost to reach that node. 

A* Search Algorithm:

Finds the shortest path to a goal node but uses both the actual cost to reach the node and a heuristic to estimate the remaining distance. Utilizes a priority queue, maintaining two scores for each node: the cost from the start (g(n)) and the estimated cost to the goal (h(n)). The algorithm explores nodes based on the sum of these two scores.


2.2). Instructions on how to run the code.

Copy and Paste the code in a python compiler
Or Clone the Github repo and Open it in VScode


2.3). Description of your approach and any challenges faced.

Approach:
Defined a grid representing open spaces and obstacles, setting the start and goal points. Implemented two pathfinding algorithms: Greedy Best-First Search and A* Search, ensuring each algorithm could explore nodes efficiently while keeping track of the paths and costs. Used a priority queue to manage the nodes to explore, allowing for optimal selections based on the heuristic for GBFS and both cost and heuristic for A*.


Challenges Faced:
- Path Reconstruction: Ensuring that the path is reconstructed correctly required careful tracking of the nodes visited.
- Performance Comparison: Timing both algorithms while ensuring fair comparisons involved careful placement of timing code.
- Understanding Heuristics: Determining a suitable heuristic (Manhattan distance) that effectively guided the search without leading to suboptimal paths was critical.


3). Screenshots: Include screenshots of the output from your program showing.

3.1). The paths found by both algorithms.

Greedy Best-First Search (GBFS):

![image](https://github.com/user-attachments/assets/090df05c-58b8-4627-b89b-96ec365ba8be)

A* Search Algorithm:

![image](https://github.com/user-attachments/assets/e8ed45a8-d54b-4cb8-9ac0-78eb449220a2)


3.2). The time taken for each algorithm.

![image](https://github.com/user-attachments/assets/46df327b-2ab2-4972-8e61-6a8032a252c5)

3.3). The lengths of the paths.

![image](https://github.com/user-attachments/assets/54212db4-754f-4df6-8c82-334f409464dc)
