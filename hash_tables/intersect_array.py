class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        else:
            hash_map = {}
            result = []
            for i, val in enumerate(nums1):
                hash_map[val] = hash_map.get(val, 0) + 1


            for i, val in enumerate(nums2):
                cnt = hash_map.get(val, 0)
                if val in hash_map and cnt > 0:
                    result.append(val)
                    cnt -=1
                    hash_map[val] = cnt
        return result  