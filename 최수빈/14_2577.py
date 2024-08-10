import sys


# 이거 나중에 다시 짜 보기
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

num = str(a * b * c)

for i in range(10):
    cnt = 0
    for n in num:
        if str(i) == n:
            cnt += 1
    print(cnt)
