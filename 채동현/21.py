import math
n = int(input())
nums = input().split(" ")
result = 0
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for i in nums:
    if is_prime(int(i)):
        result += 1
print(result)
