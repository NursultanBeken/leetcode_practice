class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hash_map=collections.defaultdict(list)
        for word in strings:
            key = []
            for i in range(len(word)-1):
                key.append( ( ord(word[i+1]) - ord(word[i]) )%26)
            hash_map[tuple(key)].append(word)
        return hash_map.values()