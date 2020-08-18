def solve(s):
    if len(s) == 0:
        return ''
    result = s[0].upper()
    ix = 1
    while ix <len(s):
        if s[ix-1] == ' ':
            result += s[ix].upper()
            ix +=1
        else:
            result += s[ix]
            ix +=1   
    return result      

if __name__ == "__main__":
    print(solve('132 456 Wq  m e'))