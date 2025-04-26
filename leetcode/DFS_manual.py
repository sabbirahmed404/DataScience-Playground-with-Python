class node:
    def __init__(self, a, b, z):
        self.x = a 
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]  # Down, Up, Left, Right
        self.y_move = [0, 0, -1, 1]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_level = 999999
        self.state = 0

    def init(self):
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [1, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]
        self.N = len(graph)
        source_x = 0
        source_y = 2
        goal_x = 4
        goal_y = 4
        self.source = node(source_x, source_y, 0)
        self.goal = node(goal_x, goal_y, self.goal_level)
        self.st_dfs(graph, self.source)

        if self.found:
            print("Goal Found")
            print("Number of steps required = ", self.goal.depth)
        else:
            print("Goal cannot be reached from source")

    def print_directions(self, m, x, y):
        if m == 0:
            print(f"Moving Down to position ({x},{y})")
        elif m == 1:
            print(f"Moving Up to position ({x},{y})")
        elif m == 2:
            print(f"Moving Left to position ({x},{y})")
        elif m == 3:
            print(f"Moving Right to position ({x},{y})")

    def st_dfs(self, graph, u):
        graph[u.x][u.y] = 0  # Mark as visited
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            # Check if within bounds and is a valid path
            if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:
                v_depth = u.depth + 1
                self.print_directions(j, v_x, v_y)
                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal.depth = v_depth 
                    return 
                child = node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)
            if self.found: 
                return
def main():
    d = DFS()
    d.init()

if __name__ == "__main__":
    main()