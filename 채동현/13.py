import sys
n = int(input())
a = [sys.stdin.readline() for _ in range(n)]
a_s = list(map(lambda x: (x.split(" ")), a))

for i in a_s:  
    total = 0
    for j in range(1, int(i[0])+1):
        total += int(i[j])
    ave = total / int(i[0])
    higher = 0
    for j in range(1, int(i[0])+1):
        if int(i[j]) > ave:
            higher += 1
    print(str(round(higher/int(i[0])*100, 3)) + "%")




