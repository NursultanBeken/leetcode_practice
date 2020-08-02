class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        print(f'y ={x}')
        print(f'y = {y}')
        while y:
            print(f'>>>>>bit y = {y}')
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
            print(f'bit x ={x}')
            print(f'bit y = {y}')
        return bin(x)[2:]

if __name__ == "__main__":
    obj1 = Solution()
    print(obj1.addBinary('1111', '10'))