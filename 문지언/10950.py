import sys
T=int(input())

nums=[list(map(int,sys.stdin.readline().split())) for _ in range(T)]

for a,b in nums:
    print(a+b)