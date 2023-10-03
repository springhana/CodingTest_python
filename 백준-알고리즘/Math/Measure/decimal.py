n = int(input())
m = list(map(int, input().split()))
result = 0
for i in m:
    data = []
    for j in range(1, i + 1):
        if i % j == 0:
            data.append(j)
    if len(data) <= 2:
        if i != 1:
            result += 1

print(result)
