##ALL Python general questions:
+ * Write a program to find avg_word_length with test cases? Avg length of words, some of the edge cases are having spaces in the beginning and end of the words, returning a float instead of int, returning None for blank input.
+ * Write a program to validate ip address with test cases ?
+ * Find common words in 2 sentences
+ * Count distinct words in a sentence
+ * Count the number of times a word appear in a sentence using a Hash Map

* Return tuples of a list, matching each item to another item
* Count the number of times a substring appear in a string

## Python Specifc question!!!

# Question 1:
# Complete a function that returns the number of times a given character occurs in the given string
# For example:
# - input string = "mississippi"
# - char = "s"
#
# - output : 4

# Question 2:
# Fill in the blanks
#
# Given an array containing None values fill in the None values
# with most recent non None value in the array

# For example:
# - input array: [1,None,2,3,None,None,5,None]
#
# - output array: [1,1,2,3,3,3,5,5]
# [1,None,1,2,None} --> [1,1,1,2,2]

=+++++++++


# Question 3:
# Complete a function that returns a list containing all the mismatched words (case sensitive) between two given input strings
# For example:
# - string 1 : "Firstly this is the first string"
# - string 2 : "Next is the second string"
#
# - output : ['Firstly', 'this', 'first', 'Next', 'second']



#Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-increasing) or not.
# -Examples:
# -// 1 2 5 5 8
# -// true
# -// 9 4 4 2 2
# -// true
# -// 1 4 6 3
# -// false





###Appendix
```
Given two sentences, construct an array that has the words that appear in one sentence and not the other.  

want you to write me a simple spell checking engine.

The query language is a very simple regular expression-like language, with one special character: . (the dot character), which means EXACTLY ONE character (it can be any character). So, for example, 'c.t' would match 'cat' as the dot matches any character. There may be any number of dot characters in the query (or none).

Your spell checker will have to be optimized for speed, so you will have to write it in the required way. There would be a one-time setUp() function that does any pre-processing you require, and then there will be an isMatch() function that should run as fast as possible, utilizing that pre-processing.

There are some examples below, feel free to ask for clarification.

Word List:

[cat, bat, rat, drat, dart, drab]

Queries:

cat -> true
c.t -> true
.at -> true
..t -> true
d..t -> true
dr.. -> true
... -> true
.... -> true

..... -> false
h.t -> false
c. -> false
*/

// write a function
// Struct setup(List<String> list_of_words)
// Do whatever processing you want here
// with reasonable efficiency.
// Return whatever data structures you want.
// This function will only run once

// write a function
// bool isMatch(Struct struct, String query)
// Returns whether the query is a match in the
// dictionary (True/False)
// Should be optimized for speed  
```