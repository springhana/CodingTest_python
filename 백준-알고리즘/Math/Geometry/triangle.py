triangle = list(map(int, input().split()))
triangle.sort()
result = triangle[0] + triangle[1] + min(triangle[0] + triangle[1] -1, triangle[2])
print(result)