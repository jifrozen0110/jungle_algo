import sys

n = int(input())
a = [sys.stdin.readline() for _ in range(n)]
for i in a:
    score = 0
    plus = 0
    prev = ""
    for j in i:
        if j == "O":
            if prev == "O":
                plus += 1
                score += plus
                score += 1
                prev = "O"
            else:
                score += 1
                prev = "O"
        else:
            plus = 0
            prev = "X"
    print(score)
        