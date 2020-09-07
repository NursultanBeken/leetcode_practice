class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_hash = {}
        if len(nums)==0:
            return False
        
        for ix, val in enumerate(nums):
            dict_hash[ val ] = dict_hash.get(val,0) + 1
        
        for item, value in dict_hash.items():
            if value > 1:
                return True
        return False