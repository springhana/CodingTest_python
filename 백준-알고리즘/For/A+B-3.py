n = int(input())
array = []

for _ in range(n):
    a, b = map(int, input().split())
    array.append(a + b)

for i in array:
    print(i)
