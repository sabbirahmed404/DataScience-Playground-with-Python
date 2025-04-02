def depth_limited_search(maze, current, target, depth, limit, visited, path):
    """
    Performs a depth-limited DFS from the current cell.
    Returns a tuple (found, path) where found is True if target is reached.
    """
    x, y = current
    # Add current cell to the path and mark as visited
    path.append(current)
    visited.add(current)
    
    # Check if we've reached the target
    if current == target:
        return True, path

    # If the current depth equals limit, backtrack.
    if depth == limit:
        path.pop()
        return False, None

    # Define possible moves: up, down, left, right.
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(maze), len(maze[0])
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        neighbor = (nx, ny)
        # Check bounds, not a wall (maze cell 0 means free) and not visited.
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and neighbor not in visited:
            found, result_path = depth_limited_search(maze, neighbor, target, depth + 1, limit, visited, path)
            if found:
                return True, result_path
    # Backtrack if no neighbor led to a solution.
    path.pop()
    return False, None


def iterative_deepening_dfs(maze, start, target, max_depth):
    """
    Uses iterative deepening DFS (IDDFS) to search for a path.
    Returns a tuple (found, found_depth, path) where:
      - found: True if a path was found.
      - found_depth: depth at which the target was found.
      - path: list of cells (tuples) representing the traversal order.
    """
    for limit in range(max_depth + 1):
        visited = set()
        path = []
        found, result_path = depth_limited_search(maze, start, target, 0, limit, visited, path)
        if found:
            return True, len(result_path) - 1, result_path  # depth = number of moves (edges)
    return False, max_depth, None


if __name__ == "__main__":
    try:
        # Read maze dimensions
        rows, cols = map(int, input("Enter number of rows and columns: ").split())
        maze = []
        print("Enter the maze grid (0 for empty, 1 for wall):")
        for _ in range(rows):
            row = list(map(int, input().strip().split()))
            maze.append(row)

        # Read start and target cells.
        # Expecting input format like: "Start: 0 0" and "Target: 2 3"
        start_input = input("Start: ").split()
        target_input = input("Target: ").split()
        start = (int(start_input[0]), int(start_input[1]))
        target = (int(target_input[0]), int(target_input[1]))

        # Set a maximum depth limit for IDDFS. (For example, rows*cols or a given max.)
        max_depth = rows * cols  # you can adjust this if needed

        found, found_depth, traversal_path = iterative_deepening_dfs(maze, start, target, max_depth)

        if found:
            print(f"Path found at depth {found_depth} using IDDFS")
            print("Traversal Order:", traversal_path)
        else:
            print(f"Path not found at max depth {max_depth} using IDDFS")
    except ValueError:
        print("Wrong Input format")
