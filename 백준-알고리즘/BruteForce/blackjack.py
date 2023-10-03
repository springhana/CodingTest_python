
n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                result = max(result, card[i] + card[j] + card[k])

print(result)

# 파이썬에서는 itertools.permutation 을 이용하면 for문 사용없이 순열을 구할 수 있다
import itertools

pool = ["A", "B", "C"]
print(list(map(''.join, itertools.permutations(pool))))  # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2))))  # 2개의 원소로 수열 만들기
