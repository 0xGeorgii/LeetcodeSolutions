class Solution:
    def makeGood(self, s: str) -> str:

        if len(s) == 1:
            return s
        
        res = []

        for i in range(len(s)):

            if len(res) == 0:
                res.append(s[i])
                continue

            c1 = s[i]
            c2 = res.pop()

            if abs(ord(c1) - ord(c2)) == 32:
                continue
            else:
                res.append(c2)
                res.append(c1)


        return "".join(res)
