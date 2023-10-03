# n, m = map(int, input().split())
#
# list = [i + 1 for i in range(n)]
#
# for _ in range(m):
#     i, j = map(int, input().split())
#     div = int(j / i / 2)
#     i -= 1
#     j -= 1
#     if div > 1:
#         for _ in range(div):
#             list[i], list[j] = list[j], list[i]
#             i += 1
#             j -= 1
#     else:
#         list[i], list[j] = list[j], list[i]
#
# for i in list:
#     print(i, end=' ')


n, m = map(int, input().split())

basket = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    temp = basket[i - 1:j]
    temp.reverse()
    basket[i - 1:j] = temp

for i in range(n):
    print(basket[i], end=' ')
