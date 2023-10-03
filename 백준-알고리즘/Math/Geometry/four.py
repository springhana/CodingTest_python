x = []
y = []
w, h = 0, 0
for _ in range(3):
    n, m = map(int, input().split())
    x.append(n)
    y.append(m)

for i in range(3):
    if x.count(x[i]) == 1:
        w = x[i]
    if y.count(y[i]) == 1:
        h = y[i]

print(w, h)
# count는 문자의 개수를 찾을 수 있다
