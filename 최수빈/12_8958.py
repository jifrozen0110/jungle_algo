import sys

input_num = int(sys.stdin.readline())
input_arr = []
for i in range(input_num):
    input_arr.append(sys.stdin.readline())


# 현 위치가 O이면
# O이면 현재값에 1 더하고

# 현 위치가 X이면
# 현재값을 0으로 초기화
for i in range(input_num):
    score = 0
    temp = 0
    for char in input_arr[i]:
        if char == 'O':
            temp += 1
            score += temp
        else:
            temp = 0

    print(score)