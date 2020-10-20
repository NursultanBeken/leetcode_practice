class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        dict_map = { '}':'{',
                    ')': '(',
                    ']':'[' }
        
        for item in s:
            if item in dict_map:
                upper_value = stack.pop() if stack else '#'
                if upper_value != dict_map[item]:
                    return False
            else:
               stack.append(item)
        
        if stack:
            return False
        else:
            return True