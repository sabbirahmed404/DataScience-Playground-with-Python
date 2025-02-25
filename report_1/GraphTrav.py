import random

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
   
    print(all_cells)
    source = random.choice(all_cells)
    goal = random.choice(all_cells)

    

    return grid, source, goal

if __name__ == "__main__":
    grid, source, goal = gridcall()
    print("Grid Size", len(grid))
    print("Grid:")
    for row in grid:
        print(row)
    print("source",source)
    print("grid",goal)