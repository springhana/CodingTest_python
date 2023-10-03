data = [0] * 11
data[1] = 1
data[2] = 2
data[3] = 4

for i in range(4, 11):
    data[i] = sum(data[i - 3:i])

n = int(input())
for _ in range(n):
    m = int(input())
    print(data[m])

# 9095번
