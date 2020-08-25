"""
303. Range Sum Query - Immutable
"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = nums
        
        # precalculate sums
        for i in range(1, len(nums)):
            self.prefixSum[i] += self.prefixSum[i-1]
            

    def sumRange(self, i, j):
        # if i = 0 return (0,j)-> prefixSum[j]
        sum = self.prefixSum[j]

        if i > 0:
            sum = self.prefixSum[j] - self.prefixSum[i-1]
        return sum
