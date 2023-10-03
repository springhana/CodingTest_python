n, m = map(int, input().split())
data = []

for i in range(1, n + 1):
    if n % i == 0:
        data.append(i)

if len(data) >= m:
    print(data[m - 1])
else:
    print(0)
