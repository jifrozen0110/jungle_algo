import sys

a = [sys.stdin.readline() for _ in range(9)]

int_a = list(map(int, a))

largest = 0
large_index = 0
for i in range(9):
    if int_a[i] >= largest:
        largest = int_a[i]
        large_index = i + 1
print(largest)
print(large_index)