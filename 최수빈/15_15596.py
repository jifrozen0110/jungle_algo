# a: list - 명시적으로 변수가 list 값임을 선언
# -> int - return 값이 int다
import sys
def solve(a: list) -> int:
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum