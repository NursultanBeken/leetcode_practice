"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for i in range(len(s)):
            v, w = s[i], t[i]
            if (v in map_s and map_s[v] != w) or (w in map_t and map_t[w] != v):
                return False
            else:
                map_s[v] = w
                map_t[w] = v
        return True    
        