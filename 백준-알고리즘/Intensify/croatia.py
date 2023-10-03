n = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
result = []
for i in croatia:
    n = n.replace(i, '*') # croatia에 있는 단어가 있다면 아무 단어로 대체한 후 길이를 구한다.
print(len(n))
