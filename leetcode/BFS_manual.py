from collections import deque

class node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.level = z

class BFS:
    def __init__(self):
        self.directions = [
            (1, 0, 'down'),   # Moving down: increase row (x)
            (-1, 0, 'up'),    # Moving up: decrease row (x)
            (0, 1, 'right'),  # Moving right: increase column (y)
            (0, -1, 'left')   # Moving left: decrease column (y)
        ]
        self.source = None
        self.goal = None
        self.found = False
        self.N = 0
        self.goal_level = 0


    def init(self):
        graph = [
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]
        self.N = len(graph)

        source_x = 0        
        source_y = 0
        goal_x = 4
        goal_y = 4
        self.source = node(source_x, source_y, 0)
        self.goal = node(goal_x, goal_y, float('inf'))

        self.st_dfs(graph)

        if self.found:
            print("Goal Found")
            print(f"Number of Moves required {self.goal_level}")
        else:
            print("Goal not found :(")

    def st_dfs(self, graph):
        queue = deque()
        queue.append(self.source)
        while queue:
            u = queue.popleft()
            for dx, dy , directions in self.directions:
                v_x = dx + u.x
                v_y = dy + u.y
                # Check if the coordinates are valid first
                if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:
                    v_level = u.level + 1
                    print(f"Moving {directions}")
                    if self.goal.x == v_x and self.goal.y == v_y:
                        self.found = True
                        self.goal_level = v_level
                        self.goal.level = v_level
                        return
                    graph[v_x][v_y] = 0
                    child = node(v_x, v_y, v_level)
                    queue.append(child)
                    if self.found:
                        return

def main():
    bfs = BFS()
    bfs.init()

if __name__ == "__main__":
    main()
