class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        result_list=[]
        
        for i in range(len(nums)):
            map[nums[i]]=i
            
        for i in range(len(nums)):
            comp = target - nums[i]
            
            if (comp in map) and (map[comp]!=i):
                result_list.extend( (i,map[comp]))
                return result_list
        