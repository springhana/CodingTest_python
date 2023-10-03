import sys

sys.setrecursionlimit(10000)
n = int(input())


def dfs(nx, ny):
    if nx <= -1 or ny <= -1 or nx >= N or ny >= M:
        return False
    if grape[nx][ny] == 1:
        grape[nx][ny] = 0
        # 상 하 좌 우
        dfs(nx - 1, ny)
        dfs(nx + 1, ny)
        dfs(nx, ny - 1)
        dfs(nx, ny + 1)
        return True
    return False


for _ in range(n):
    M, N, K = map(int, input().split())
    grape = [[0] * M for _ in range(N)]
    result = 0
    for i in range(K):
        x, y = map(int, input().split())
        grape[y][x] = 1

    for col in range(N):
        for row in range(M):
            if dfs(col, row):
                result += 1
    print(result)
