# Fill in the blanks
#
# Given an array containing None values fill in the None values
# with most recent non None value in the array

# For example:
# - input array: [1,None,2,3,None,None,5,None]
#
# - output array: [1,1,2,3,3,3,5,5]
# [1,None,1,2,None} --> [1,1,1,2,2]

def fillBlanks(input_list):
    for index, value in enumerate(input_list):
        if not value:
            input_list[index] = input_list[index-1]
    return input_list


# Complete a function that returns the number of times a given character occurs in the given string
# For example:
# - input string = "mississippi"
# - char = "s"
#
# - output : 4

def charOccurs(s, ch):
    cnt = 0
    for item in s:
        if item == ch:
            cnt +=1
    return cnt


# Write a program to find avg_word_length with test cases? 
# Avg length of words, some of the edge cases are having spaces in the beginning and end of the words, 
# returning a float instead of int, returning None for blank input.

def avg_word_length(sentence):
    """
    "Hit myt nam ist Bob" ->
    "   Hi my name is Bob  " -> 
    "    " -> None
    sentence = input("Please enter a sentence: ")
    """
    if len(sentence) == 0:
        return None
    words = sentence.split()
    filtered_out = [item for item in words if item.isalnum()]
    if len(filtered_out) == 0:
        return None
    average=1.0 * sum(len(word)for word in filtered_out)/len(filtered_out)
    return average





if __name__=="__main__":
    case1 = fillBlanks([1,None,2,3,None,None,5,None])
    print(case1)
    case2 = fillBlanks([1, None, None, None, None])
    print(case2)
    case3 = fillBlanks([ None, None, None, None])
    print(case3)    
    case4 = fillBlanks([ None])
    print(case4)  
    count = charOccurs('abccdefgaa','a')
    print(f'count ={count}')
    count1 = 'mississippi'.count('s')
    print(count1)
    print(avg_word_length("Hi my name is Bob"))
    print(avg_word_length("   Hi my name is Bob  "))
    print(avg_word_length("  "))
    print(avg_word_length(""))
    print(avg_word_length("   Hi my name is Bob  !"))
    print(avg_word_length("Hir mye nam ist Bob"))
    print(avg_word_length("Bo 5"))
    print(avg_word_length("!"))