class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_lenght = len(num1)
        num2_lenght = len(num2)
        
        i = num1_lenght - 1
        num1_int = 0
        for char in num1:
            print(char)
            num1_int += (ord(char)-ord('0') )*(10**i)
            i=i-1
        print(num1_int)
        
        j = num2_lenght - 1
        num2_int = 0
        for char in num2:
            num2_int += (ord(char)-ord('0') )*(10**j)
            j=j-1
        print(num2_int)
        return num1_int + num2_int

if __name__ == "__main__":
    obj1 = Solution()
    print(obj1.addStrings('17', '9'))            