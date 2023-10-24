# 자주 나오는 단어인가
# 해당 단어 길이가 긴다.
# 일파벳 순
# M보다 길이가 작으면 무시
import sys

n, m = map(int, sys.stdin.readline().split())
array = {}
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= m:
        if word not in array:
            array[word] = 1 + (round(len(word) * 0.000001, 6))
        else:
            array[word] += 1
array = sorted(array.items())
array = sorted(array, key=lambda i: i[1], reverse=True)
for i in array:
    print(i[0])
