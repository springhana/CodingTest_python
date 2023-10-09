n, m = map(int, input().split())

# 맵
data = []
for _ in range(n):
    data.append(list(map(int, input())))

# 방문 처리할 맵
visited = [[0] * m for _ in range(n)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if data[x][y] == 0:
        data[x][y] = 1
        for d in range(4):
            dfs(x + dx[d], y + dy[d])
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
