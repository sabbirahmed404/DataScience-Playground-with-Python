import random
from collections import deque

def dfs_pathfinding(grid, source, goal):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]
    stack = deque()
    topological_order = []
    
    stack.append(source)
    visited[source[0]][source[1]] = True
    found = False
    
    # Directions: up, right, down, left
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    
    while stack:
        current = stack.pop()
        topological_order.append(current)
        
        if current == goal:
            found = True
            break
            
        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    parent[nx][ny] = current
                    stack.append((nx, ny))
    
    # Reconstruct path if found
    path = []
    if found:
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node[0]][node[1]]
        path.reverse()
        
    return path, topological_order

def gridcall():
    N = random.randint(4,7)
    #grid = [[0 for _ in range(N)] for _ in range(N)]
    grid = []
    for i in range(N):
        row = []
        for j in range (N):
            row.append(0)
        grid.append(row)

    all_cells = [] 
    for i in range(N):
        for j in range (N):
            all_cells.append((i,j)) 
   
    #print(all_cells)
    source = random.choice(all_cells)
    goal = random.choice(all_cells)
    while goal == source:
        goal = random.choice(all_cells)

    for i in range(N):
        for j in range(N):
            if (i,j) != goal and (i,j) != source:
                if random.random() < 0.2:
                    grid[i][j] = 1




    return grid, source, goal

def visualize_path(grid, path):
    # Create a copy of grid to add path markers
    grid_copy = [row.copy() for row in grid]
    for (i,j) in path:
        grid_copy[i][j] = '*'
    return grid_copy

if __name__ == "__main__":
    grid, source, goal = gridcall()
    path, topo_order = dfs_pathfinding(grid, source, goal)
    
    print(f"Grid Size: {len(grid)}")
    print("Initial Grid:")
    for row in grid:
        print(row)
        
    print("\nSource:", source)
    print("Goal:", goal)
    
    if path:
        print("\nDFS Path:")
        marked_grid = visualize_path(grid, path)
        for row in marked_grid:
            print(row)
        print("\nPath Coordinates:", path)
    else:
        print("\nNo path found!")
        
    print("\nTopological Order of Traversal:")
    print(topo_order)