class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vovels = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }
        r, l = 0, 0

        for i in range(len(s)):
            c = s[i]
            if c in vovels:
                if i < len(s) // 2: r += 1
                else: l += 1

        return r == l
