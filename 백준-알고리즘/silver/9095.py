n = int(input())
data = [0] * 11
data[0] = 1
data[1] = 2
data[2] = 4

for i in range(3, 11):
    data[i] = sum(data[i - 3:i])

for j in range(n):
    a = int(input())
    print(data[a-1])
