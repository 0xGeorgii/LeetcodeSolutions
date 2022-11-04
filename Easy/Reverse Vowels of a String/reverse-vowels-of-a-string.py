class Solution:
    def reverseVowels(self, s: str) -> str:

        left = len(s)
        vovels = "AEIOUaeiou"
        s = list(s)

        for i in range(len(s)):

            if s[i] in vovels:

                while left != i:                    
                    left -= 1
                    if s[left] in vovels:
                        break

                t = s[i]
                s[i] = s[left]
                s[left] = t
            
            if i == left:
                break

        return "".join(s)
