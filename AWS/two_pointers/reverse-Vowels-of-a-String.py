class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        
        if len(s) == 0:
            return s
        else:
            l, r = 0, len(s) - 1
            s = [i for i in s]
            while l < r:
                while l < r and s[l] not in vowels:
                    l +=1
                while l < r and s[r] not in vowels:
                    r -=1
                s[l], s[r] = s[r], s[l]
                l +=1
                r -=1
                
            return "".join(s)     
                
                    
                    
        