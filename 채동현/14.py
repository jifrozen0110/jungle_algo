import sys

a = [sys.stdin.readline() for _ in range(3)]

multiple = 1
for i in a:
    multiple *= int(i)

multiple_s = str(multiple)
result = [0 for _ in range(10)]
for i in range(len(multiple_s)):
    result[int(multiple_s[i])] += 1

for i in range(10):
    print(result[i])