x, y, w, h = map(int, input().split())
data = [x, y, w - x, h - y]

print(min(data))