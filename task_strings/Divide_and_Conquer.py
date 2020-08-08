""" A solution template for the divide and conquer problems :

Define the base case(s).

Split the problem into subproblems and solve them recursively.

Merge the solutions for the subproblems to obtain the solution for the original problem. """

"""53. Maximum Subarray """
def maxSubArray( nums) :
    """brute force O(n^3) """
    max_sum = -99999      
    for left in range(len(nums)):
        
        for right in range(left,len(nums)):
            print(f'left = {left}')
            print(f'right = {right}')
            print(nums[left:right+1])
            wind_sum = sum( nums[left:right+1] )
            print(f'wind_sum = {wind_sum}')
            max_sum = max(max_sum, wind_sum)
    return max_sum
    
    def maxSubArray2(self, nums: List[int]) -> int:
        """Dynamic Programming (Kadane's algorithm) """
        
        max_sofar = nums[0]
        global_max = nums[0]
        
        for i in range(1, len(nums)):     
            max_sofar = max(nums[i], nums[i]+max_sofar) 
            global_max = max(max_sofar, global_max )
            
        return global_max

if __name__ == "__main__":
    print(maxSubArray([-2,1]))
