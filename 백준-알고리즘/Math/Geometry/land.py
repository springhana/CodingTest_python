x = []
y = []
w, h = 0, 0
a = int(input())

for _ in range(a):
    n, m = map(int, input().split())
    if a == 1:
        print(0)
    else:
        x.append(n)
        y.append(m)
if a != 1:
    w = max(x) - min(x)
    h = max(y) - min(y)
    print(w * h)
