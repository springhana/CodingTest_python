#  재귀함수로 구하는 법
# n = int(input())
# def fibonacci(n):
#     global a
#     global b
#     if n == 0:
#         a += 1
#         return 0
#     elif n == 1:
#         b += 1
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for i in range(n):
#     N = int(input())
#     a = 0
#     b = 0
#     fibonacci(N)
#     print(a, b)

#  파보니치 규칙을 이용
zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(n):
    if len(zero) <= n:
        for i in range(len(zero), n + 1):
            zero.append(zero[i - 2] + zero[i - 1])
            one.append(one[i - 2] + one[i - 1])
    return zero[n], one[n]


n = int(input())
for _ in range(n):
    a, b = fibonacci(int(input()))
    print(a, b)
