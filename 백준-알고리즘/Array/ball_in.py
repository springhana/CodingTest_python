n, m = map(int, input().split())
basket = [0 for i in range(n)]

for _ in range(m):
    ball = list(map(int, input().split()))

    for i in range(ball[0] - 1, ball[1]):
        basket[i] = ball[2]

for i in basket:
    print(i, end=' ')
