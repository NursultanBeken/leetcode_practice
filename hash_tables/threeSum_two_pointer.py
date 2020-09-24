class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort list to apply two pointer solution
        nums.sort()
        res = []
        for i in range(len(nums)):
            # If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
            if nums[i] > 0:
                break
            # If the current value is the same as the one before, skip it   
            if i == 0 or nums[i-1] != nums[i]:
                self.twosum2(nums, i, res)
        return res   
    
    def twosum2(self, nums, i, res):
        left, right = i+1, len(nums)-1    
        while left < right:
            target = nums[i] + nums[left] + nums[right]      
            if target < 0:
                left +=1
            elif target > 0:
                right -=1
            else:
                # Otherwise, we found a triplet
                res.append([nums[i], nums[left], nums[right]])
                left +=1
                right -=1
                while left < right and nums[left] == nums[left-1]:
                    left +=1