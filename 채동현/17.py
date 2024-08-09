import sys

n = int(input())

a = [sys.stdin.readline() for _ in range(n)]

for i in a:
    result = ""
    nums = i.split(" ")
    for j in nums[1]:
        if j != '\n':
            s = j * int(nums[0])
            result += s
    print(result)

