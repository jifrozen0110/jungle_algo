import sys

T,b=map(int,sys.stdin.readline().split())

nums=list(map(int,sys.stdin.readline().split()))

for num in nums:
    if num<b:
        print(f'{num}',end=' ')

print()