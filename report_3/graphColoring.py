def read_input(filename):
    # Open the input file
    file = open(filename, "r")
    # Read the first line and extract N (vertices), M (edges), and K (colors)
    line = file.readline()
    parts = line.split()
    n = int(parts[0])
    m = int(parts[1])
    k = int(parts[2])
    
    # Initialize an n x n adjacency matrix with 0's
    graph = []
    i = 0
    while i < n:
        row = []
        j = 0
        while j < n:
            row.append(0)
            j += 1
        graph.append(row)
        i += 1

    # Read the next m lines and add the undirected edges to the adjacency matrix
    edge_count = 0
    while edge_count < m:
        line = file.readline()
        if line == "":
            break
        parts = line.split()
        if len(parts) < 2:
            continue
        u = int(parts[0])
        v = int(parts[1])
        graph[u][v] = 1
        graph[v][u] = 1
        edge_count += 1

    file.close()
    return n, k, graph

def is_safe(vertex, graph, colors, color):
    # Check for every vertex if there is an edge from vertex to that vertex 
    # and if that vertex has the same color.
    i = 0
    while i < len(graph):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
        i += 1
    return True

def graph_coloring_util(graph, k, colors, vertex, n):
    # Base case: If all vertices are assigned a color then return True
    if vertex == n:
        return True

    # Try assigning each color from 1 to k
    color = 1
    while color <= k:
        if is_safe(vertex, graph, colors, color):
            colors[vertex] = color
            if graph_coloring_util(graph, k, colors, vertex + 1, n):
                return True
            # Backtrack
            colors[vertex] = 0
        color += 1

    return False

def graph_coloring(filename):
    # Read the graph input from file
    n, k, graph = read_input(filename)
    
    # Initialize color assignment for all vertices (0 means no color)
    colors = []
    i = 0
    while i < n:
        colors.append(0)
        i += 1

    # Start backtracking from the first vertex
    if graph_coloring_util(graph, k, colors, 0, n):
        print("Coloring Possible with", k, "Colors")
        print("Color Assignment:", colors)
    else:
        print("Coloring Not Possible with", k, "Colors")

# Example of how to call the function
# Change "input.txt" to the filename containing your input.
if __name__ == "__main__":
    graph_coloring("report_3/input.txt")
