import sys

n = int(sys.stdin.readline())

array = []
stack = []
for _ in range(n):
    num = sys.stdin.readline().rstrip()
    # 1 X: 정수 X를 스택에 넣는다.
    if num[0] == "1":
        stack.append(num[2:]) # 두자리 수일 경우 주의
    # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    elif num[0] == "2":
        if stack:
            array.append(stack.pop())
        else:
            array.append(-1)
    # 3: 스택에 들어있는 정수의 개수를 출력한다.
    elif num[0] == "3":
        array.append(len(stack))
    # 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif num[0] == "4":
        if stack:
            array.append(0)
        else:
            array.append(1)
    # 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif num[0] == "5":
        if stack:
            array.append(stack[len(stack) - 1])
        else:
            array.append(-1)

for i in array:
    print(i)
