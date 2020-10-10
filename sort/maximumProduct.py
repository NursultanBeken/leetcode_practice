class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        max_product = max( nums[0] * nums[1] * nums[len(nums)  - 1],
                          nums[len(nums)  - 1] * nums[len(nums)  - 2] * nums[len(nums) - 3] )
            
        return max_product    