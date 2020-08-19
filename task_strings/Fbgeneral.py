"""
Example Python Syntax (will also be provided during the interview)

Loops
for x in l: "Iterate on x for each value in list"
for i in range(0,5): "Iterate on i from value 0 to 4"
for k, v in d.items(): "Iterate on each key, value pair in dict"

Lists (Array)
l = [] "Define an empty list"
l[i] "Return value at index i in list"
len(l) "Return length of list"
l.append(x) "Add value x to the end of list"
l.sort() "Sort values in list - in place sort, returns None"
sorted(l) "Return sorted copy of list"
x in l: "Evaluate True if x is contained in the list"

Dictionary (HashMap)
d = {} "Define an empty Dictionary"
d[x] "Return value for key x"
d[x] = 1 "Set value for key x to 1"
d.keys() "Return list of keys"
d.values() "Return list of values"

Tuple
tup = ()
tup = (1,2) + tup

Other functions
reversed(n) "reverse a list"
random.random() "random number between 0 and 1"
random.randrange(start, stop) "Return a randomly selected element from range(start, stop)"
isinstance(x, list) "returns True if x is instance of list"
split() "returns a list of all the words in the string"
ceil() "returns the smallest integer value greater than or equal to x"
"""

"""
Write a function that returns the elements on odd positions (0 based) in a list
"""
def solution(input):
    #code goes here
    output = [ input[i] for i in range(len(input)) if i%2!=0]
    return output

assert solution([0,1,2,3,4,5]) == [1,3,5]
assert solution([1,-1,2,-2]) == [-1,-2]


"""
Write a function that returns the cumulative sum of elements in a list
"""
def solution2(input):
    # Code goes here
    for i in range(1, len(input)):
        input[i] += input[i-1]
    output = input[:]
    print(output)
    return output

assert solution2([1,1,1]) == [1,2,3]
assert solution2([1,-1,3]) == [1,0,3]

"""
Write a function that takes a number and returns a list of its digits
"""
def solution3(input):
    # Code goes here
    output = [ int(digit) for digit in str(input)]
    return output

assert solution3(123) == [1,2,3]
assert solution3(400) == [4,0,0]

"""
From: http://codingbat.com/prob/p126968
Return the "centered" average of an array of ints, which we'll say is 
the mean average of the values, except ignoring the largest and 
smallest values in the array. If there are multiple copies of the 
smallest value, ignore just one copy, and likewise for the largest 
value. Use int division to produce the final average. You may assume 
that the array is length 3 or more.
"""
def centered_average(nums):
  aveg = (sum(nums) - max(nums) - min(nums)) / (len(nums)-2)
  return aveg

assert centered_average([1, 2, 3, 4, 100]) == 3
assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
assert centered_average([-10, -4, -2, -4, -2, 0]) == -3


