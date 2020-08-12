def sum13(nums):
  if len(nums) == 0:
    return 0
  if nums[0]!=13:
      cnt = nums[0] 
  else:
       cnt = 0
  for ix in range(1, len(nums)):
    if nums[ix] !=13 and nums[ix-1] !=13:
      cnt +=nums[ix]
  print(cnt)    
  return cnt


def sum67(nums):
  if len(nums) == 0:
    return 0
  total = sum(nums)
  ix_6 = 0
  for i in range(len(nums)):
    if nums[i] == 6 and i>=ix_6:
      ix_6 = i
      while nums[ix_6] != 7:
        total -=nums[ix_6]
        ix_6 +=1
      total = total - nums[ix_6]
  print(total)    
  return total   

if __name__ == "__main__":
    sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7])
