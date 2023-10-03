word = input().upper()
word_list = list(set(word))
cut = []

for i in word_list:
    count = word.count(i)
    cut.append(count)

if cut.count(max(cut)) >= 2:
    print("?")
else:
    print(word_list[cut.index(max(cut))]) # cut.index <= cut index 찾기(제일 큰 수)
