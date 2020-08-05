class Solution:
    def isMonotonic(self, A) -> bool:
        
        # [1,2,3,1,4,1] [5,4,3,2,1,5] [1,1,1,2,1,1,1]
        
        if len(A) == 1:
            return True
        
        p1 = 0
        p2 = len(A) - 1
        
        if A[p1] < A[p2]:
            # check that for all i<=j A[i]<=A[j]
            while p1 < len(A) -1:
                if A[p1] > A[p1+1]:
                    return False
                else:
                    p1 +=1
        elif A[p1] > A[p2]:
            # check that for all i<=j A[i]>=A[j]
            while p1 < len(A) -1:
                if A[p1] < A[p1+1]:
                    return False
                else:
                    p1 +=1
            
        else:
            # A[p1] = A[p2]
            if len(A) != A.count(A[p1]):
                return False
            
        return True