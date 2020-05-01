# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
# [1, 2, 3, 4, 5]
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #return min ( version for version in range(1,mid+1) if isBadVersion(version) )
        # binary search
        left = 1
        right = n
        while left < right:
            mid = left + (right - left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid +1
        return left
