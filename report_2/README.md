# Iterative Deepening Depth-First Search (IDDFS) Implementation

This directory contains the implementation and documentation for Iterative Deepening Depth-First Search (IDDFS) algorithms as part of Lab Report 2.

## Contents

- `AI_Lab_Lab_Report_2.pdf` - Detailed lab report documenting the implementation, analysis, and results of the IDDFS algorithms
- `IDDFS.py` - Implementation of IDDFS for maze pathfinding problems
- `iterative_deepening.py` - Implementation of IDDFS for graph traversal problems

## Overview

Iterative Deepening Depth-First Search (IDDFS) is a state space/graph search strategy that combines the benefits of Breadth-First Search's completeness and Depth-First Search's memory efficiency. The algorithm works by performing a series of depth-limited searches, gradually increasing the depth limit until the goal is found.

## Features

- **Maze Pathfinding** (`IDDFS.py`): Finds a path from a start position to a target position in a 2D maze
- **Graph Traversal** (`iterative_deepening.py`): Performs IDDFS on a graph represented as an adjacency matrix

## Usage

### Maze Pathfinding

```python
# Run the maze pathfinding implementation
python IDDFS.py

# Input format:
# - Number of rows and columns
# - Maze grid (0 for empty, 1 for wall)
# - Start position coordinates
# - Target position coordinates
```

### Graph Traversal

```python
# Run the graph traversal implementation
python iterative_deepening.py

# Input format:
# - Number of nodes in the graph
# - Adjacency matrix
# - Destination node
```

## Algorithm Details

IDDFS works by running a depth-limited search with increasing depth limits until the goal is found. This approach:

1. Ensures completeness (like BFS)
2. Uses memory efficiently (like DFS)
3. Finds the optimal solution when all edges have the same cost

For more detailed information about the implementation and analysis, please refer to the PDF report.
