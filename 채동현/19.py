nums = input().split(" ")

f = nums[0][::-1]
s = nums[1][::-1]

if int(f) > int(s):
    print(f)
else:
    print(s)