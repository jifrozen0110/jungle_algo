import sys

def long_str(str):
    cnt, txt = str.split()
    result_str = ''
    for t in txt:
        result_str += t * int(cnt)
    return result_str

cnt = int(sys.stdin.readline())
result_arr = [long_str(sys.stdin.readline()) for _ in range(cnt)]

print(*result_arr, sep='\n')