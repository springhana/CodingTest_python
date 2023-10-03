n, m = map(int, input().split())
result = list(map(int, input().split()))

print(sorted(result, reverse=True)[m - 1])
