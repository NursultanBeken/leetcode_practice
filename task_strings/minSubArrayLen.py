"""
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s.
 If there isn't one, return 0 instead.
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, total = 0, 0
        min_sum = len(nums) + 1
        
        for i, val in enumerate(nums):
            total += val
            while total >= s:
                min_sum = min(min_sum, i + 1 - left)
                total -= nums[left]
                left +=1
        return min_sum if min_sum <= len(nums) else 0
        
        
        