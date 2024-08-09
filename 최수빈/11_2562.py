import sys

arr = []
max_val = 0
max_locate = 0
for i in range(9):
    arr.append(int(sys.stdin.readline()))
    if max_val < arr[i]:
        max_val = arr[i]
        max_locate = i+1

print(max_val)
print(max_locate)
