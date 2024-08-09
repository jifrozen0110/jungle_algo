import sys

n = input()
a = [sys.stdin.readline() for _ in range(int(n))]

for i in a:
    num_s = i.split(' ')
    print(int(num_s[0]) + int(num_s[1]))



