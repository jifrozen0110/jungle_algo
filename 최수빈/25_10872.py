# N! N*(N-1)*(N-2)*...*1
import sys
sys.setrecursionlimit(10**8)

def recursive(n):
    if n > 0:
        return n * recursive(n-1)
    else:
        return 1

innum = int(sys.stdin.readline())
result = recursive(innum)

print(result)