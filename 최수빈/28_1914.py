# 이게 원판 한 묶음 씩 이동시키는.. 그런거네

import sys
sys.setrecursionlimit(10**8)

def move(no, x, y):
    if no > 1:
        move(no-1, x, 6-x-y)

    print(x, y)
    
    if no > 1:
        move(no-1, 6-x-y, x)

cnt = int(sys.stdin.readline())

print(2**cnt - 1)

if cnt <= 20:
    move(cnt, 1, 3)