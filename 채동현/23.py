import sys

n = int(sys.stdin.readline())

def hansu(n):
    if n < 100:
        return True
    
    if n >= 1000:
        return False
    
    str_n = str(n)
    if int(str_n[1]) * 2 == int(str_n[0]) + int(str_n[2]):
        return True
    
result = 0
for i in range(1, n+1):
    if hansu(i):
        result += 1
print(result)
