# Python program to check whether it is possible to make 
# string palindrome by removing one character 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_range_pal(low, high, ins):
            while low < high:
                if ins[low] != ins[high]:
                    return False
                else:
                    low +=1
                    high -=1
            return True       
            
        left,right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                if is_range_pal(left+1, right, s):
                    return True
                if is_range_pal(left, right-1, s):
                    return True 
                return False
        return True