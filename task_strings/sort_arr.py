class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        output_arr=[]
        
        for i in arr1:
            if (i in arr2) and (i in arr3):
                output_arr.append(i)
        sorted_arr = sorted(output_arr,reverse=False)      
        return sorted_arr

if __name__ == "__main__":
    obj1 = Solution()
    print(obj1.arraysIntersection( [1,2,3,4,5], [1,2,5,7,9],[1,3,4,5,8]))