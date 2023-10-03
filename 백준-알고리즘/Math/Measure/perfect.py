while True:
    data = []
    word = ""
    n = int(input())
    if n == -1:
        break
    for i in range(1, n + 1):
        if n % i == 0:
            data.append(i)
    if n == (sum(data) - n):
        for j in range(len(data) - 1):
            if j != 0:
                word = word + " + " + str(data[j])
            else:
                word += str(data[j])
        print(str(n) + " = " + word)
    else:
        print(str(n) + " is NOT perfect.")
