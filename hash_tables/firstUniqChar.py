class Solution:
    def firstUniqChar(self, s: str) -> int:
        #build hashmap
        hash_map = {}
        
        for idx, ch in enumerate(s):
            hash_map[ch] = hash_map.get(ch,0) + 1
        
        for idx, ch in enumerate(s):
            if hash_map[ch]==1:
                return idx
        return -1