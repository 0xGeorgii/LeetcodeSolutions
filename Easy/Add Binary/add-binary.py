class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l, la, lb = 0, len(a), len(b)

        if la > lb:
            d = la - lb
            b = ("0" * d) + b
            l = la
        elif lb > la:
            d = lb-la
            a = ("0" * d) + a
            l = lb
        else:
            l = la

        res = [""] * l
        m = 0

        for i in range(l-1, -1, -1):

            i1, i2 = int(a[i]), int(b[i])
            s = i1 + i2 + m

            if s == 1:
                res[i] = "1"
                m = 0
            elif s == 2:
                res[i] = "0"
                m = 1
            elif s > 2:
                res[i] = "1"
                m = 1
            else:
                res[i] = "0"
                m = 0
        
        res = "".join(res)
        if m > 0:
            res = "1" + res
        
        return res
