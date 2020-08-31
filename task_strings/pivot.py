def pivotIndex(nums):
    left_sum = 0
    right_sum = sum(nums) - nums[0]
 
    for i in range(1, len(nums)):
        left_sum += nums[i-1]
        right_sum -= nums[i]
        print(f'left_sum = {left_sum}, right_sum={right_sum}')
        if left_sum == right_sum:
            return i
    return -1  

if __name__ == "__main__":
    pivotIndex([-1,-1,-1,0,1,1])