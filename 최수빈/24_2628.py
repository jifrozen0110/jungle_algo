# 접근방법
# 넓이를 구하는 것은 결국 가로 세로 변의 길이를 알아내야 함
# 주어진 좌표를 이용해서 가로 세로 길이의 배열을 구하고
# 이 값들을 곱한 넓이 결과 중 가장 큰 것을 반환

# 접근을 잘못했따!!!!
# 0, 3 이면 0이 가로 선
# 1, 4이면 1이 세로선

import sys


# 좌표를 순회하면서 빼자
x, y = sys.stdin.readline().split()

innum = int(sys.stdin.readline())
coordinates = [sys.stdin.readline().strip().split() for _ in range(innum)]

print(f'x: {x}, y: {y}')
print(coordinates)

# x 좌표 비교
coord_x = [0]
coord_y = [0]
for i in range(innum):
    print(f'{i}번째 순회중')
    if (coordinates[i][0] == '0'):
        coord_y.append(int(coordinates[i][1]))
    else:
        coord_x.append(int(coordinates[i][1]))

coord_x.append(int(x))
coord_y.append(int(y))

coord_x.sort()
coord_y.sort()

print(f'x 좌표들: {coord_x}, y 좌표들: {coord_y}')

# 넓이 저장
extent =[]
for i in range(len(coord_x)-1):
    len_x = coord_x[i+1] - coord_x[i] # x 길이
    # print(f'x의 길이: {len_x}')
    for i in range(len(coord_y)-1):
        len_y = coord_y[i+1] - coord_y[i]
        # print(f'y의 길이: {len_y}')
        # print(f'x*y = {len_x*len_y}')
        extent.append(len_x*len_y)

print(max(extent))



