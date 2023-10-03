dial_char = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', ""]
dial_num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n = input()
result = 0
for i in n:
    for j in range(len(dial_char)):
        if i in dial_char[j]:
            result += dial_num[j]

print(result)
