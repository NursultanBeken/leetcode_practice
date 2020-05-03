import pdb
import collections

class Solution:
    """
    Runtime: 176 ms
    Memory Usage: 14.2 MB

    Runtime: 92 ms
    Memory Usage: 13.9 MB

    Runtime: 48 ms
    Memory Usage: 14.1 MB

    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = 0
        map = []
        for val in magazine:
            map.append(val)

        for x in ransomNote:
            #pdb.set_trace()
            if x in map:
                map.remove(x)
                count = count +1
            else:
                return False
        return True

        
    def canConstruct_better(self, ransomNote: str, magazine: str) -> bool:

        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # In Python, we can use the Counter class. It does all the work that the
        # makeCountsMap(...) function in our pseudocode did!
        magazine_counts = collections.Counter(magazine)
        ransom_note_counts = collections.Counter(ransomNote)

        # For each *unique* character in the ransom note:
        for char, count in ransom_note_counts.items():
            # Check that the count of char in the magazine is equal
            # or higher than the count in the ransom note.
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False

        # If we got this far, we can successfully build the note.
        return True

obj = Solution()
result = obj.canConstruct_better('aa','aab')
print(result)
