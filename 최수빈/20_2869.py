import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

# 낮에 a 올라가고
# 밤에 b 내려가고
# 높이는 v
# locate = 0
# day = 0

# while locate < int(v):
#     day += 1
#     locate += int(a)
#     if locate >= int(v):
#         break
#     locate -= int(b)

# print(day)


# 어찌되었든 마지막날에는 올라가기만 할거야
# 그러니까 마지막날 전까지 올라갈 거리를 v-a라고 구할 수 있고
# 하루 순수 이동거리는 a-b 니까
# 이걸 나누면 됨

day = math.ceil((v-a) / (a-b)) + 1
print(day)