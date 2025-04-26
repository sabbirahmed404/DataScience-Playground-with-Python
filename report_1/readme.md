# Graph Traversal with DFS

#### Task
```task
 Write a program that generates a random N×N grid (N between 4 and 7) with non-obstacle source and goal states. It performs DFS to find a path from source to goal and prints the grid, source, goal, DFS path, and topological order of node traversal.
```

A Python implementation that generates random grids (4x4 to 7x7) with obstacles and performs depth-first search (DFS) pathfinding between source/goal nodes. Features include obstacle avoidance (20% density), path visualization with '*' markers, and topological traversal order tracking.

**Key Features:**  
- Randomized grid generation with distinct source/goal  
- 4-directional DFS pathfinding  
- Visualized path output and traversal diagnostics  
- CLI display of grid configuration/path coordinates  

**Usage:**  
```bash
python GraphTrav.py
```
Sample output includes initial grid, marked path (if found), and node visitation order. Run multiple times to see different grid configurations.

**Dependencies:** Python 3.6+, `random`, `collections.deque`


