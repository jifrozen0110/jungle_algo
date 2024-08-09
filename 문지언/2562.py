import sys

nums=[int(sys.stdin.readline()) for _ in range(9)]

maxinum=max(nums)
print(maxinum)
print(nums.index(maxinum)+1)

# maxinum=nums[0]

# answer=0;

# for index,num in enumerate(nums):
#     if maxinum<num:
#         maxinum=num
#         answer=index


# print(maxinum)
# print(index)