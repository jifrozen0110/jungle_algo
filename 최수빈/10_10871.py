# 10871_X보다 작은 수
# 정수 N개로 이루어진 수열 A와 정수 X가 주어지면
# A에서 X보다 작은 수 모두 출력하기

import sys

n_str, x_str = sys.stdin.readline().split()
n = int(n_str)
x = int(x_str)

input_str = sys.stdin.readline().split()
arr = []
for i in range(n):
    arr.append(int(input_str[i]))

result_arr = []
for i in range(n):
    if x > arr[i]:
        result_arr.append(arr[i])

# astarisk * : 언패킹 연산자
print(*result_arr)
