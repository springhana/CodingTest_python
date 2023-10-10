n = int(input())
word = []

for _ in range(n):
    a = input()
    if word.count((len(a), a)) == 0:
        word.append((len(a), a))

b = sorted(word)

for i in b:
    num, chat = i
    print(chat)
