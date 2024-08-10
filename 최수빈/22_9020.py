# 주어진 짝수보다 큰 소수는 없을 것
# 그래서 주어진 수보다 작은 소수를 모두 찾고
# 그걸 빼서 확인하나?
import sys

# 소수 여부 판별
def check_num(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def goldbach(n):
    # 돌면서 빼보고 소수인지 확인해서 return
    num = int(n)
    for i in range(2, num//2 + 1):
        if check_num(i) and check_num(num-i):
            return i, num-i

count = int(sys.stdin.readline())
nums = [sys.stdin.readline().strip() for _ in range(count)]


for n in nums:
    g1, g2 = goldbach(n)
    print(f'{g1} {g2}')