n = int(input())

# for a in range(n):
#     for b in range(a + 1):
#         print("*",end='')
#     print("")

for a in range(n):
    for _ in range(n - (a + 1)):
        print(" ", end='')
    for _ in range(a + 1):
        print("*", end='')
    print("")
