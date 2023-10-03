word = []
for _ in range(5):
    word.append(input())

for row in range(max(len(e) for e in word)):
    for col in range(5):
        if row < len(word[col]):
            print(word[col][row], end='')
