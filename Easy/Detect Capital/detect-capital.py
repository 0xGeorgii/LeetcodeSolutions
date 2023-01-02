class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word) == 1: return True

        all_capitals = word[0] in string.ascii_uppercase and word[1] in string.ascii_uppercase
        all_lowers = word[0] in string.ascii_lowercase
        mixed = word[0] in string.ascii_uppercase and word[1] in string.ascii_lowercase

        if all_capitals:
            for c in word:
                if c not in string.ascii_uppercase:
                    return False
        elif all_lowers:
            for c in word:
                if c not in string.ascii_lowercase:
                    return False
        elif mixed:
            for c in word[1:]:
                if c not in string.ascii_lowercase:
                    return False
        else:
            return False

        return True
