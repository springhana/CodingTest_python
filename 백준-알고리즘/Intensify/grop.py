n = int(input())
result = 0
for _ in range(n):
    word = input()
    count = 0
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            new_word = word[i + 1:]
            if new_word.count(word[i]) > 0:
                count += 1
    if count == 0:
        result += 1

print(result)