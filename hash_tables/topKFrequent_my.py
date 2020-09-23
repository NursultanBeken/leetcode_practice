class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        result = []
        for ix, val in enumerate(nums):
            hash_map[val] = hash_map.get(val, 0) + 1
            
        sort_orders = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        
        for i in sort_orders[:k]:
            result.append(i[0])
        return result    