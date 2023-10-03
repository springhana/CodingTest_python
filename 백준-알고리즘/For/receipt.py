all_money = int(input())
n = int(input())
result = 0

for _ in range(n):
    money, x = map(int, input().split())
    result += (money * x)

if result == all_money:
    print("Yes")
else:
    print("No")
