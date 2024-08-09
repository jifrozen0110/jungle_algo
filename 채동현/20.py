import math
n = input().split(" ")

print(math.ceil((int(n[2]) - int(n[0])) / (int(n[0]) - int(n[1]))) + 1)