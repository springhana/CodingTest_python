a, b = map(int, input().split())
c = int(input())

time = a * 60 + b + c
a = int(time / 60)
b = time % 60

if a >= 24:
    a = a % 24

print(a, b)

# 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.
