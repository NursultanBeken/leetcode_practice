class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        cur_index = 0
        search_ix = 0

        
        for cur_index in range(1, len(nums)):
            if nums[search_ix] != nums[cur_index]:
                for i in (search_ix+1,cur_index):
                    nums[i] = nums[cur_index]
                search_ix = search_ix+1
        return search_ix+1