# 평균을 구해서 점수와 비교하고 평균을 넘는 사람을 구해서 비율 구하기

import sys

input_num = int(sys.stdin.readline())
result_arr = []
for i in range(input_num):
    line_val = list(map(int, sys.stdin.readline().split()))
    avg = sum(line_val[1:]) / line_val[0]  # 평균 계산

    # 평균 넘는 인원수 구하기
    student = 0
    for score in line_val[1:]:
        # 평균과 value값 비교
        if score > avg: 
            student += 1

    # 비율 구하기
    ratio = student/line_val[0]*100
    # result_arr.append(str(round(ratio, 3)) + '%')
    result_arr.append(f"{ratio:.3f}%")

print(*result_arr, sep='\n')


