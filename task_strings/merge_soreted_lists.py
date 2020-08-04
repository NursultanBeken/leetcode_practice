

def mergeSorted(s1, s2, m, n):
    # pointers to the begining of each list
    p1, p2 =0, 0

    # create copy and empty s1 as we are going to put a result there
    s1_copy = s1[:m]
    s1[:] = []

    while p1 < m and  p2 < n:
        if s1_copy[p1] < s2[p2]:
            s1.append(s1_copy[p1])
            p1 +=1
        else:
            s1.append(s2[p2])
            p2 +=1   
    #if there is still something left in the list
    if p1 < m:
        s1[p1+p2:] = s1_copy[p1:]
    if p2 < n:
        s1[p1+p2:] = s2[p2:]

    return s1

if __name__=='__main__':
    result = mergeSorted([1,2,3,0,0,0], [2,5,6], 3 ,3)
    print(result)
