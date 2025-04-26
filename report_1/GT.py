import random

def generate_grid():
    # Randomly select grid size between 4 and 7
    N = random.randint(4, 7)
    
    # Create empty grid
    grid = [[0 for _ in range(N)] for _ in range(N)]
    
    # Generate all possible coordinates
    all_cells = [(i, j) for i in range(N) for j in range(N)]
    
    # Randomly select distinct source and goal positions
    source = random.choice(all_cells)
    goal = random.choice(all_cells)
    while goal == source:
        goal = random.choice(all_cells)
    
    # Add random obstacles (20% probability) avoiding source/goal positions
    for i in range(N):
        for j in range(N):
            if (i, j) != source and (i, j) != goal:
                if random.random() < 0.2:
                    grid[i][j] = 1
                    
    return grid, source, goal

if __name__ == "__main__":
    grid, source, goal = generate_grid()
    print("Grid Size:", len(grid))
    print("Grid:")
    for row in grid:
        print(row)
    print("Source:", source)
    print("Goal:", goal)
