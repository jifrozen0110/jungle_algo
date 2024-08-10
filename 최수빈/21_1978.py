# 소수: 1과 자기 자신만을 인수로 갖는 수. 1은 소수가 아님.
# 그럼 1부터 그 수만큼 증가시켜서 나머지가 있는지 확인하면 될듯

import sys

count = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
result = 0

for num in nums:
    cnt = 0
    if num == 1:
        continue
    if num == 2:
        result += 1
        continue
    for i in range(2, num):
        if num % i == 0:
            cnt += 1
    if cnt == 0:
        result += 1
            
    

print(result)