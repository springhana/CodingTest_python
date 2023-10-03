import sys
sys.setrecursionlimit(10000)
T = int(input())
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= N or y >= M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for w in range(4):
            dfs(x + dx[w], y + dy[w])
        return True
    return False


for _ in range(T):
    M, N, K = map(int, input().split())
    result = 0
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for B in range(N):
        for L in range(M):
            if dfs(B, L):
                result += 1
    print(result)
