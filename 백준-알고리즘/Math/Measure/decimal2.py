n = int(input())
m = int(input())
result = []

for i in range(n, m + 1):
    count = 0
    data = []
    for j in range(1, i + 1):
        if i % j == 0:
            data.append(i)
    if len(data) <= 2:
        if i != 1:
            result.append(i)

if len(result) < 1:
    print(-1)
else:
    print(sum(result))
    print(result[0])
