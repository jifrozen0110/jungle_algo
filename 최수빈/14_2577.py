import sys


# 이거 나중에 다시 짜 보기
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

num = str(a * b * c)

arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# 배열에 1~9 숫자를 담아두고
# number 배열을 돌리면서 같은지 비교한 뒤에
# 같으면 cnt 를 증가
for i in range(9):
    cnt = 0
    for n in num:
        if arr[i] == n:
            cnt += 1
    # print(arr[i])
    print(cnt)
