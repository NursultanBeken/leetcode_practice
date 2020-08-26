"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                return nums[i-1] + 1  