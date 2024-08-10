import sys

# 한수 판별
def find_num(num):
    if len(num) == 1 or len(num) == 2:
        return True
    diff = 0
    for i in range(len(num)-1):
        # 등차수열이니까 3개의 값만 비교하면 되지않나
        # 근데 일의자리, 십의자리 숫자까지는 다 등차수열일듯
        # 백의자리부터 탐색

        # 첫번째 순회에서 차이값 저장
        if i == 0:
            diff = int(num[i]) - int(num[i+1])
            continue
        # 두번째 이후부터 차이값 비교
        else:
            # 차이값이 저장한 값과 다르면 False
            if int(num[i]) - int(num[i+1]) != diff:
                return False
            else:
                # 마지막 순서면 True 리턴
                if i == len(num)-2:
                    return True
                else:
                    continue




innum = int(sys.stdin.readline().strip())

# 한수를 찾는 함수를 만들어서
# 1 부터 1000까지 탐색

cnt = 0
for i in range(1, innum+1):
    if find_num(str(i)):
        cnt += 1

print(cnt)
