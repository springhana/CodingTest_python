n, m = map(int, input().split())
a, b, d = map(int, input().split())

visited = [[0] * m for _ in range(n)]  #  방문 표시 할 맵
visited[a][b] = 1

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = a + dx[d]
    ny = b + dy[d]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if visited[nx][ny] == 0 and data[nx][ny] == 0:
        visited[nx][ny] = 1
        a = nx
        b = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = a - dx[d]
        ny = b - dy[d]
        # 뒤로 갈 수 있다면 이동하기
        if data[nx][ny] == 0:
            a = nx
            b = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)
