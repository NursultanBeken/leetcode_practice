class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        result = []
        
        if len(nums) == 0:
            return result
        else:
            l = 0
            r = 0
            
            while l < len(nums):
                r = l
                while r < len(nums) - 1 and nums[r] +1 == nums[r+1]:
                    r +=1
                if l == r:
                    result.append(str(nums[l]))
                else:
                    result.append(str(nums[l]) + "->" + str(nums[r]) ) 
                l = r + 1
              
            return result    
                
                     
        