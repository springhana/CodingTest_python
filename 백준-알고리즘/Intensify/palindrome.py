# from collections import deque
#
# text = input()
# palindrome = ""
# queue = deque()
# for i in text:
#     queue.append(i)
#
# for i in range(len(queue)):
#     palindrome += queue.pop()
#
# if text == palindrome:
#     print("1")
# else:
#     print("0")

word = list(str(input()))

if list(reversed(word)) == word: #reverssed는 배열을 역순으로 해준다
    print(1)
else:
    print(0)