class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return str
        
        return "".join([ w[::-1] + " " for w in s.split(" ")])[:-1]
