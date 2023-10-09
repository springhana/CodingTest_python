array = [6, 5, 3, 1, 8, 7, 2, 4]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]:  # 한 칸씩 왼족으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 머
            break

print(array)
