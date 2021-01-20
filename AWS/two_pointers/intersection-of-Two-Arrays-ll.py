class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        sorted_1 = sorted(nums1)
        sorted_2 = sorted(nums2)
        
        p1, p2, k = 0, 0, 0
        
        while (p1 < len(sorted_1) and p2 < len(sorted_2)):
            if sorted_1[p1] < sorted_2[p2]:
                p1 +=1
            elif sorted_1[p1] > sorted_2[p2]:
                p2 +=1
            else:
                sorted_1[k] = sorted_1[p1]
                p2 +=1
                p1 +=1
                k +=1
                
        return  sorted_1[:k]      
        