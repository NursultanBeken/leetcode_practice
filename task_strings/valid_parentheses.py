class Solution:
    def is_valid(self, s: str) -> bool:

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:

            # if char is one of the closing brackets
            if char in mapping:
                # pop the top element
                # if stack is empty then assign '#' which will never be in the string
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False
            else:
                # add new opening bracket into the stack
                stack.append(char)

        # if stack is NOT empty then the input string is NOT valid
        # if stack is empty then the input string is valid
        if stack:
            return False
        else:
            return True
