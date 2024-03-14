n = int(input())
m = int(input())
result = 0

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited_dfs = [0] * (n + 1)


def dfs(start):
    global result
    visited_dfs[start] = 1
    result += 1
    for i in range(1, n + 1):
        if visited_dfs[i] == 0 and graph[start][i] == 1:
            dfs(i)


dfs(1)
print(result - 1)
