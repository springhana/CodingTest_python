while True:
    number = list(map(int, input().split()))
    number.sort()
    if 0 in number:
        break
    elif number[2] >= number[1] + number[0]:
        print("Invalid")
    elif number[0] == number[1] == number[2]:
        print("Equilateral")
    elif number[0] == number[1] or number[0] == number[2] or number[1] == number[2]:
        print("Isosceles")
    else:
        print("Scalene")
