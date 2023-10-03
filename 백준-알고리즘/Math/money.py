change = [25, 10, 5, 1]
n = int(input())

for _ in range(n):
    money = int(input())
    for i in range(len(change)):
        print(money // change[i], end=' ')
        money %= change[i]
