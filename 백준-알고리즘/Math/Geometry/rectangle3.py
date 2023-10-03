data = []
result = 0
word = ""
for _ in range(3):
    n = int(input())
    data.append(n)
    result += n

if result == 180:
    for i in range(len(data)):
        if data.count(data[i]) == 3:
            word = "Equilateral"
        elif data.count(data[i]) == 2:
            word = "Isosceles"
        else:
            word = "Scalene"
else:
    word = "Error"

print(word)
