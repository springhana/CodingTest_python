import sys

n = int(sys.stdin.readline())
result = []

for _ in range(n):
    vps = sys.stdin.readline()
    for i in range(len(vps)):
        vps = vps.replace('()', '')
    if len(vps) == 1:
        print("YES")
    else:
        print("NO")
