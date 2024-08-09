import sys

n = sys.stdin.readline()

for i in range(int(n)):
    star = "*"
    for j in range(i):
        star += "*"
    print(star)   