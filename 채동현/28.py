# hanoi(n원반, 어디서, 경유, 어디로): 
#     if n==1 : move(n번원반, 어디서, 어디로)
#     hanoi(n-1번원반, 어디서, 경유, 어디로)
#     move(n원반,어디서?,어디로)
#     hanoi(n-1원반, 경유, 어디서, 어디로 )

import sys
n = int(sys.stdin.readline())
def hanoi(n, start, middle, end):
    if n == 1:
        return print(f"{start} {end}")
    hanoi(n-1, start, end, middle)
    print(f"{start} {end}")
    hanoi(n-1, middle, start, end)

if n > 20:
    print(2**n-1)
else:
    print(2**n-1)
    hanoi(n, 1, 2, 3)
