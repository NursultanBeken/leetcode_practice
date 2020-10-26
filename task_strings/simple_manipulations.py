s = 'missisipi'

find_s= s.find('s')
count_s=s.count('s')
index_s=s.index('s')

print(f'find >>> {find_s}' )
print(f'count >>> {count_s}')
print(f'index >>> {count_s}')



input_list = [None]
test_list = [1, None, 1, 2, None]
print(f'before: {input_list}')  
# [1,None,1,2,None] --> [1,1,1,2,2]
for index, value in enumerate(input_list):
    if not value:
        input_list[index] = input_list[index-1]

print(input_list)  

test_list = [1, None, 1, 2, None]
print ("The original list is : " + str(test_list)) 
res = [i for i in test_list if i] 
print ("List after removal of None values : " +  str(res)) 



#find the average length of word in sentence
sentence = "Hi my name is Bob"
words = sentence.split()
print(words)
average=1.0* sum(len(word)for word in words)/len(words)
print(average)



#for a list array=[['D'],['A','B'],['A','C'],['C','A']] find the number of followers
#Ans
#D=0
#A=2
#c=1
arr = [['D'],['A','B'],['A','C'],['C','A']]
print(arr)
user_dict = {}
print(len(arr))
if len(arr) ==0:
        print("")
for i in range(len(arr)):
        cnt = 0
        val = arr[i][0] 
        # if this is the first time we meet the user     
        if val not in user_dict:
                if len(arr[i]) == 1:
                        user_dict[val]=0
                else:
                        user_dict[val]=1    
        else:
                if len(arr[i]) != 1:
                        user_dict[val] +=1
print(user_dict)                        


arr = [1,3,4,5,8]

for i in arr:
        print(i)

if 3 in arr:
        print('tess')