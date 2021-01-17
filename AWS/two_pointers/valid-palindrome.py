class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            filtered = [ i.lower() for i in s if i.isalnum() ]
            l = 0
            r = len(filtered) - 1
            
            while (l<r):
                if filtered[l] == filtered[r]:
                    l +=1
                    r -=1
                else:
                    return False
            return True