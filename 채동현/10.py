import sys

a = [sys.stdin.readline() for _ in range(2)]

first = a[0].split(" ")
second = a[1].split(" ")
result = ""
for i in range(int(first[0])):
    if int(second[i]) < int(first[1]):
        result += (second[i])
        result += " "
print(result)