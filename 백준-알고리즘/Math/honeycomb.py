n = int(input())

home = 1
count = 1

while n > home:
    home += 6 * count
    count += 1

print(count)