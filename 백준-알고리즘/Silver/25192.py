n = int(input())

result = 0
array = [[] for i in range(n)]
index = 0
for _ in range(n):
    a = input()
    if a != "ENTER":
        array[index].append(a)
    else:
        index += 1

for i in range(len(array)):
    array[i] = set(array[i])
    result += len(array[i])

print(result)