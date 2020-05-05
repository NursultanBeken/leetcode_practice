"""
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),
 and its complement is 010. So you need to output 2
"""
import pdb
class Solution:
    def findComplement(self, num: int):
        if num == 1:
            return 0
        elif num == 0:
            return 1
        binary_input = format(num, "b")
        result = []
        for digit in binary_input:
            #pdb.set_trace()
            if digit == '0':
                result.append('1')
            elif digit == '1':
                result.append('0')
        bin_result = ''.join(result)
        return int(bin_result,2)


obj = Solution()
lst = obj.findComplement(7)
print(lst)
