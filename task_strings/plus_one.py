class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        addetive = 0
        last_ix = len(digits)-1
        
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits 
        return [1]+digits