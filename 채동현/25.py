import sys
n = int(sys.stdin.readline())

def fac(n, count):
    if n < 2:
        return count
    return fac(n-1, n*count)

print(fac(n, 1))