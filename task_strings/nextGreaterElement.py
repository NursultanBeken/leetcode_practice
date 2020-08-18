def nextGreaterElement( nums1, nums2):
    map_d, stack, ans = {}, [], []
    
    for x in nums2:
        while len(stack) and stack[-1] < x:
            map_d[stack.pop()] = x
        stack.append(x)

    for x in nums1:
        ans.append(map_d.get(x, -1))
            
    return ans