n, m = map(int, input().split())
result = 0
for _ in range(n):
    card = list(map(int, input().split()))
    result = max(result, min(card))

print(result)