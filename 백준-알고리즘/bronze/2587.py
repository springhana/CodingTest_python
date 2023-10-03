result = []
for _ in range(5):
    result.append(int(input()))

result.sort()
print(int(sum(result) / 5))
print(result[2])
