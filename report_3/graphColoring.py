def read_input(filename):

    with open(filename, "r") as file:
        first_line = file.readline().strip()
        if not first_line:
            raise ValueError("Empty file")
        n, m, k = map(int, first_line.split())
        
        G = [[0 for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, file.readline().split())
            G[u][v] = 1
            G[v][u] = 1  
    return n, k, G

def is_safe(vertex, color, colors, G):

    n = len(G)
    for i in range(n):
        if G[vertex][i] == 1 and colors[i] == color:
            return False
    return True

def m_coloring(vertex, n, m_colors, colors, G):

    if vertex == n:
        return True
    for color in range(1, m_colors + 1):
        if is_safe(vertex, color, colors, G):
            colors[vertex] = color  
           
            if m_coloring(vertex + 1, n, m_colors, colors, G):
                return True
            
            colors[vertex] = 0
    return False

def solve_graph_coloring(filename):
    n, m_colors, G = read_input(filename)
    colors = [0] * n 
    
    if m_coloring(0, n, m_colors, colors, G):
        print(f"Coloring Possible with {m_colors} Colors")
        print("Color Assignment:", colors)
    else:
        print(f"Coloring Not Possible with {m_colors} Colors")


if __name__ == "__main__":
    input_filename = "report_3/input.txt"
    solve_graph_coloring(input_filename)
