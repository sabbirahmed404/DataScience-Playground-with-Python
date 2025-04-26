def dfs_rec(adj, visited, s):
    visited[s] = True

    print(s, end=" ")

    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)


def dfs(adj, s):
    visited = [False] * len(adj)
    dfs_rec(adj, visited, s)


def add_edge(adj, t, s):
    adj[t].append(s)
    adj[s].append(t)


if __name__ == "__main__":
    V =5
    adj = [[] for _ in range(V)]
    print(adj)
    edges = [[1,2], [1,0], [2,0], [2,3], [2,4]]

    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 1
    print("DFS from source: ", source)
    dfs(adj, source)
    print((adj))