# N-Queens Problem Solver using Genetic Algorithm

This project implements a genetic algorithm approach to solve the classic N-Queens problem as part of an AI Lab assignment.

## Problem Definition

The N-Queens problem requires placing N chess queens on an N×N chessboard so that no two queens threaten each other. In other words, no two queens can share the same row, column, or diagonal.

## Objective

To find a valid configuration where N queens can be placed on an N×N board without any conflicts.

## Methods Used

- **Genetic Algorithm** with the following components:
  - **Representation**: Permutation encoding where each chromosome is a list of integers representing queen positions
  - **Fitness Function**: Counts the number of diagonal conflicts (fewer is better)
  - **Selection**: Elitism-based selection that preserves the best solutions
  - **Crossover**: Order Crossover (OX1) to create valid permutations
  - **Mutation**: Swap mutation that exchanges positions of two queens
  - **Termination**: Either a solution is found or maximum generations reached

## Implementation

The algorithm is implemented in Python and visualizes the solution as a chessboard with queens represented by 'Q'.
