n = input()
n_list = list(n)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
result = [-1 for i in range(len(alphabet))]
for i in range(len(n_list)):
    for j in range(len(alphabet)):
        if n_list[i] == alphabet[j]:
            if result[j] != -1:
                continue
            else:
                result[j] = i

for i in result:
    print(i,end=' ')
