class Solution:
    def printVertically(self, s: str) -> List[str]:

        arr = s.split()
        ml = len(max(arr, key = len))
        res = []

        print(arr)
        for i in range(ml):
            r = ""
            for s in arr:
                if i >= len(s):
                    r += " "
                else:
                    r += s[i]

            res.append(r.rstrip())

        return res
