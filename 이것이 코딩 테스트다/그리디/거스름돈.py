n = int(input())  # 거스름 돈
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]  # 500원, 100원, 50원, 10원 배열에 담기

for coin in array:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin  # 만약 500원 이라면 거스름 돈에서 나머지 값만 구해 주고 n에 저장.

print(count)