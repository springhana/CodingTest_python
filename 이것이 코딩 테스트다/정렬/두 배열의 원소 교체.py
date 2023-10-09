n, k = map(int, input().split())
array = []

for _ in range(2):
    array.append(list(map(int, input().split())))

array[0].sort()
array[1].sort(reverse=True)

for i in range(k):
    if array[0][i] < array[1][i]:
        array[0][i], array[1][i] = array[1][i], array[0][i]
    else:
        break

print(sum(array[0]))
