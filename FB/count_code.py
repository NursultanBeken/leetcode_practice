"""
Return the number of times that the string "code" appears 
anywhere in the given string, except we'll accept any letter 
for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""
def count_code(str):
    x=["co"+i+"e" for i in str.lower()]
    count = 0
    index = 0
    print(x)
    for i in x:
        print(i)
        if i in str[index:]:
            print(str[index:])
            index = str.find(i)+1
            count+=1
    return count


"""
Return the number of times that the string "hi" appears anywhere in the given string.
"""
def count_hi(str):
  sum = 0
  ## Loop to length-1 and access index i and i+1
  ## in the loop.
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      sum = sum + 1
  return sum



"""
Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string

"""
def end_other(a, b):
  if len(a) > len(b):
    # b should be in the end of a
    if a[-len(b):].lower() == b.lower():
      return True
  else:
    if b[-len(a):].lower() == a.lower():
      return True
      
  return False



if __name__ == "__main__":
    result = count_code('cozexxcope')
    print(f'answer =  {result}')

