num_list = []
div_list = []

for _ in range(10):
    a = int(input())
    num_list.append(a)

for i in num_list:
    div = i % 42
    if div_list.__contains__(div):
        continue
    else:
        div_list.append(div)

print(len(div_list))