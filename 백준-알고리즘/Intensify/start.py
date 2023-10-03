n = int(input())

for i in range(1, n):
    print(' '*(n - i) + "*"*(i * 2 - 1))
for i in range(n,0,-1):
    print(' '*(n - i) + "*"*(i * 2 - 1))


# for i in range(1, n+1):
#     for _ in range(n - i):
#         print(" ", end='')
#     for _ in range(i):
#         print("*", end='')
#     for _ in range(i-1):
#         print("*", end='')
#     for _ in range(n - i):
#         print(" ", end='')
#     print()
#
#
# for s in range(1,n):
#     for _ in range(s):
#         print(" ", end='')
#     for _ in range(n-s):
#         print("*", end='')
#     for _ in range(n-s-1):
#         print("*", end='')
#     for _ in range(s):
#         print(" ", end='')
#     print()
