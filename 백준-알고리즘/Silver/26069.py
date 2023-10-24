n = int(input())
array = ["ChongChong"]

for _ in range(n):
    a, b = map(str, input().split())
    if array.__contains__(a) > 0:
        array.append(b)
    elif array.__contains__(b) > 0:
        array.append(a)

print(len(set(array)))
