# 2438_별 찍기 - 1
# 입력한 숫자만큼 별을 찍자
import sys

input_num = int(sys.stdin.readline())

for i in range(1, input_num+1):
    print('*' * i)

# for i in range(input_num):
#     print_star = ''
#     # 별을 늘려가면서 찍을거야
#     for j in range(i+1):
#         print_star += '*'
#     print(print_star)
