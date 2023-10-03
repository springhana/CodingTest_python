result = 0
total = 0
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
score_A = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
for _ in range(20):
    subject = list(map(str, input().split()))
    for i in range(len(score_A)):
        if subject[2] == score_A[i]:
            if subject[2] == "P":
                continue
            else:
                result += float(subject[1]) * score[i]
                total += float(subject[1])

print(format(result / total, ".6f"))
