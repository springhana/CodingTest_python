data = input()
value = []
number = 0

# 문자를 하나씩 확인하며
for i in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if i.isalpha():
        value.append(i)
    # 숫자는 따로 더하기
    else:
        number += int(i)

# 알파벳을 오름차순으로 정렬
value.sort()

# 출력
print(''.join(value),end='')
print(number)

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
# if number != 0:
#     value.append(str(number))

# 최종 결과 출력(리스트를 문자열로 반환하여 출력)
# print(''.join(value))