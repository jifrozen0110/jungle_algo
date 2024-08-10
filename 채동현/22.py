import sys
import math

n = int(sys.stdin.readline())
a = [sys.stdin.readline() for _ in range(n)]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_gold(num1, num2):
    if is_prime(num1) and is_prime(num2):
        return num1, num2
    return find_gold(num1-1, num2+1)

for i in a:
    x, y = find_gold(int(int(i)/2), int(int(i)/2))
    print(f"{x} {y}")