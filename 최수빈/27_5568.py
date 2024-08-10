# 수를 만들고 결과값을 배열에 담아서
# 만들어진 수가 기존에 있는지 확인하는 식으로 진행해야할듯
# 그러면 수 만드는건 재귀로... 가야하나
import sys
sys.setrecursionlimit(10**8)

def make_numbers(num, depth):
    if depth == k:
        numbers.add(num)
        return
    
    for i in range(n):
        if not used[i]:
            used[i] = True
            make_numbers(num + cards[i], depth+1)
            used[i] = False

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = [sys.stdin.readline().strip() for _ in range(n)]

# set 정의
numbers = set()

used = [False] * n

make_numbers('', 0)

print(len(numbers))