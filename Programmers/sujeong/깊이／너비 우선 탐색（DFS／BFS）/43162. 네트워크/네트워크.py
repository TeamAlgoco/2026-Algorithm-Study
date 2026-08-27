def solution(n, computers):
    visited = [False] * n
    def dfs(u):
        visited[u] = True
        for v in range(n):
            if computers[u][v] == 1 and not visited[v]:
                dfs(v)
    networks = 0
    for i in range(n):
        if not visited[i]:
            networks += 1
            dfs(i)
    return networks