class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums
        else:
            k = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[k], nums[i] = nums[i], nums[k]
                    k +=1
            return nums