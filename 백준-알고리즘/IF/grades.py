a = int(input())
grades = ""

if a >= 90:
    grades = "A"
elif a >= 80:
    grades = "B"
elif a >= 70:
    grades = "C"
elif a >= 60:
    grades = "D"
else:
    grades = "F"

print(grades)
