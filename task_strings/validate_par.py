def validate(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    print(mapping.keys())
    for char in s:
        print(f'processing {char}')
        # if char is closing parenthesis then pop up the element from stack
        if char in mapping:
            print(f' {char} is in the mapping')
            # if stack is empty assigt #
            top_element = stack.pop() if stack else '#'
            
            if mapping[char] != top_element:
                return False
        else:
            # add element into stack
            stack.append(char)
    if stack:
        print('not valid')
    else:
        print('valid')

if __name__ == "__main__":
    s='((((()(('
    validate(s)
