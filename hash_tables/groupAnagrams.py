class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map=collections.defaultdict(list)
        for word in strs:
            key = sorted(word)
            hash_map[ tuple(key)].append(word)
        
        return hash_map.values()