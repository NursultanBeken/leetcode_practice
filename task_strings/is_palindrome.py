class Solution:
    def char_filter(self,input):
         return input.isalnum()
    
    def make_lower(self, input):
        return input.lower()

    def isPalindrome(self, s: str) -> bool:
        filtered_out = filter(self.char_filter, s)
        lowercase_filtered_chars = tuple(map(self.make_lower, filtered_out))

        filtered_chars_list = list(lowercase_filtered_chars)
        reverse_list = filtered_chars_list[::-1]
        return filtered_chars_list==reverse_list

if __name__ == "__main__":
    obj1 = Solution()
    print(obj1.isPalindrome('A man, a plan, a canal: Panama')) 
