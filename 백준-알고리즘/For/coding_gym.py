import math

n = int(input())
result = ""
byte = math.ceil(n / 4)

for _ in range(byte):
    result += "long "

result += "int"
print(result)