# Graph Coloring Algorithm Implementation

This directory contains the implementation and documentation for the Graph Coloring problem as part of Lab Report 3.

## Contents

- `aiLabReport_3.pdf` - Detailed lab report documenting the implementation, analysis, and results of the Graph Coloring algorithm
- `graphColoring.py` - Implementation of the Graph Coloring algorithm using backtracking
- `input.txt` - Sample input file with a small graph
- `input_2.txt` - Sample input file with a larger graph

## Overview

Graph Coloring is a well-known NP-complete problem where the goal is to assign colors to the vertices of a graph such that no two adjacent vertices have the same color. The implementation in this directory uses a backtracking approach to solve the graph coloring problem with a given number of colors.

## Algorithm Details

The implementation uses a backtracking algorithm with the following components:

- **Backtracking Function (`m_coloring`)**: Recursively tries different color assignments for each vertex
- **Safety Check (`is_safe`)**: Verifies if a color can be assigned to a vertex without violating the constraint that adjacent vertices must have different colors
- **Input Parsing (`read_input`)**: Reads the graph structure and constraints from an input file

The time complexity of this algorithm is O(m^n) in the worst case, where m is the number of colors and n is the number of vertices.

## Input Format

The input files follow this format:
- First line: Three integers `n m k`
  - `n`: Number of vertices (0 to n-1)
  - `m`: Number of edges
  - `k`: Number of available colors
- Next m lines: Two integers `u v` representing an edge between vertices u and v

## Usage

```python
# Run the graph coloring algorithm
python graphColoring.py

# By default, it uses the input.txt file in the report_3 directory
# You can modify the input_filename variable in the main function to use a different input file
```

## Example

For the input:
```
4 5 3
0 1
0 2
1 2
1 3
2 3
```

This represents a graph with:
- 4 vertices (0, 1, 2, 3)
- 5 edges
- 3 available colors

The algorithm will determine if the graph can be colored using at most 3 colors, and if possible, it will output the color assignment for each vertex.

## Applications

Graph coloring has numerous applications including:
- Register allocation in compilers
- Scheduling problems
- Frequency assignment in wireless networks
- Map coloring

For more detailed information about the implementation, analysis, and results, please refer to the PDF report.
