class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        if len(s) == 0:
            return s
        else:
            k=0
            s = list(s)
            n = len(s)
            for i in range(n):
                if s[i] not in vowels:
                    s[k] = s[i]
                    k +=1
                    
            return "".join(s[:k])      
                    
            