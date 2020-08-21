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


#import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        result_list=[]
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")  
        words=paragraph.lower().split()
        #words = [x.strip(',') for x in paragraph.lower().split()]  
        for word in words:
            if word not in banned:
                result_list.append(word)
        return max(set(result_list), key = result_list.count) 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        my_set = {}
        start,max_length = 0,0

        for i in range(n):
            if (s[i] in my_set) and (start <= my_set[s[i]]):
                start =  my_set[s[i]] + 1
            else:
                max_length = max(max_length, i - start +1)
            my_set[s[i]] = i
        return  max_length   


class WordDictionary:
    def __init__(self):
        self.d = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        self.d[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        m = len(word)
        for dict_word in self.d[m]:
            i = 0
            while i < m and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False

if __name__=="__main__":
    print(findCommon("This is document  tick  tick one one", "I get doc one is"))
    result = UncommonWords("Firstly this is the first string", "Next is the second string")
    print(f'UncommonWords = {result}')

    print(countDitinct('hehe hehe lolo jam rain rainbow Rain'))

    print(countSubstr('Lalalskdsladksd', 'la'))