class Solution:

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        arr = [ i for i in range(26)]

        def union(c1, c2):
            nonlocal arr
            a = find(c1)
            b = find(c2)

            if a > b:
                arr[a] = b
            else:
                arr[b] = a

        def find(c):
            if arr[c] != c:
                return find(arr[c])
            return c

        for i in range(len(s1)):
            union(ord(s1[i]) - 97, ord(s2[i]) - 97)
        
        res = ""
        for c in baseStr:
            res += chr(find(ord(c) - 97) + 97)

        
        return res
