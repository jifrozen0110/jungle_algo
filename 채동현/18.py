s = input()

result = 0
s_spl = s.split(" ")

for i in s_spl:
    if i != "":
        result += 1
print(result)

