class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 1:
            return ransomNote in magazine
        for c in magazine:
            if c in ransomNote:
                ransomNote = ransomNote.replace(c, '', 1)
            if len(ransomNote) == 0:
                return True
        return False
