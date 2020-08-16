"""  Find common words in 2 sentences
"""
def findCommon(s1, s2):
    s1_set = set( s1.split())
    s2_set = set( s2.split())
    common = s1_set.intersection(s2_set)
    unique = (s1_set^s2_set)
    print(f'unique = {unique}')
    return common


"""
Given two sentences as strings A and B. 
The task is to return a list of all uncommon words. 
A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence.
"""

def UncommonWords(s1, s2):
    count = {}
    for word in s1.split():
        count[word.lower()] = count.get(word.lower(), 0) + 1
    for word in s2.split():
        count[word.lower()] = count.get(word.lower(), 0) + 1
    
    return [ word for word in count if count[word]==1]

""" 
Count distinct words in a sentence
"""
def countDitinct(s):

    s_set = set( x.lower() for x in s.split())
    print(s_set)
    return len(s_set)
    
"""
Count the number of times a substring appear in a string
000123000123, 123 -> 2
>>> nStr = '000123000123'
>>> nStr.count('123')
"""
def countSubstr(str, sub):
    return str.count(sub)

if __name__=="__main__":
    print(findCommon("This is document  tick  tick one one", "I get doc one is"))
    result = UncommonWords("This", "I this")
    print(f'UncommonWords = {result}')

    print(countDitinct('hehe hehe lolo jam rain rainbow Rain'))

    print(countSubstr('Lalalskdsladksd', 'la'))