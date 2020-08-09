nums = [0,1,0,3,12]

nums_copy = nums[:]
nums = []
for ix, val in enumerate(nums_copy):
    if val != 0:
        nums.append(val)

nums[ix:] = [0 for i in range(0,len(nums_copy)-ix+1)]


print(ix)
print(nums)        