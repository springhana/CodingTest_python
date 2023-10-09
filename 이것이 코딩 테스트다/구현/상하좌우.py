# N = int(input())
# data = list(map(str, input().split()))
#
# # 상 하 좌 우
# nx = [-1, 1, 0, 0]
# ny = [0, 0, -1, 1]
# move_plan = ['U', "D", "L", "R"]
#
#
# def move(x, y):
#     dx, dy = x, y
#     for i in data:
#         for j in range(len(move_plan)):
#             if i == move_plan[j]:
#                 dx = x + nx[j]
#                 dy = y + ny[j]
#             if dx < 1 or dy < 1 or N < dx or N < dy:
#                 continue
#             x, y = dx, dy
#     return x, y
#
#
# x, y = move(1, 1)
# print(x, y)

# 책
n = int(input())
x, y = 1, 1
plans = input().split()

# 좌 우 상 하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]
nx, ny = 0, 0

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
