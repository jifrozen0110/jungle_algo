import sys
w, h = sys.stdin.readline().split(" ")

n = int(sys.stdin.readline())
a = [sys.stdin.readline().split(" ") for _ in range(n)]

w_a = list()
w_a.append(int(h))
h_a = list()
h_a.append(int(w))
for i in a:
    if i[0] == "0":
        w_a.append(int(i[1]))
    else:
        h_a.append(int(i[1]))

def largest_diff(a: list) -> int:
    a.append(0)
    a.sort(reverse=True)
    largest = 0
    for i in range(len(a)-1):
        if abs(a[i] - a[i+1]) > largest:
            largest = abs(a[i] - a[i+1])
    return largest

print(largest_diff(w_a)*largest_diff(h_a))
