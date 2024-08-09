import sys

case_val = int(sys.stdin.readline())
for i in range(case_val):
    input_str = sys.stdin.readline().split()
    print(str(int(input_str[0]) + int(input_str[1])))