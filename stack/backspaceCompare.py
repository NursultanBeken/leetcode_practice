class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        s_stack = []
        for item in S:
            if item=='#':
                if s_stack: 
                    s_stack.pop()
            else:
                s_stack.append(item)
        t_stack = []
        for item in T:
            if item=='#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(item)
                
         
        return s_stack==t_stack