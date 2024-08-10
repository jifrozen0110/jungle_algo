# 주어진 짝수보다 큰 소수는 없을 것
# 그래서 주어진 수보다 작은 소수를 모두 찾고
# 그걸 빼서 확인하나?
import sys

# 소수 여부 판별
def check_num(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1): # 책 읽어보기
        if num % i == 0:
            return False
    return True

def goldbach(n):
    # 돌면서 빼보고 소수인지 확인해서 return
    num = int(n)
    # for i in range(2, num//2 + 1):
    for i in range(num//2, 2, -1): 
        if check_num(i) and check_num(num-i):
            return min(i, num-i), max(i, num-i)
    return None

count = int(sys.stdin.readline())
nums = [sys.stdin.readline().strip() for _ in range(count)]

for n in nums:
    if n == '4':
        print('2 2')
    else:
        g1, g2 = goldbach(n)
        print(f'{g1} {g2}')