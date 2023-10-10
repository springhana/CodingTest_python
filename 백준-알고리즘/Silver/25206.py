grade = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
grade_num = [4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0]
result = 0
n = 0
for i in range(20):

    arr = list(map(str, input().split()))
    if arr[2].upper() == "P":
        continue
    for j in range(len(grade)):
        if arr[2] == grade[j]:
            result += float(arr[1]) * grade_num[j]
            n += float(arr[1])

print(format(result / n, ".6f"))
