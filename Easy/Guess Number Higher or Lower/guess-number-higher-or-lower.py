class Solution:
    def guessNumber(self, n: int) -> int:

        l = 1
        res = guess(l)
        if res == 0: return l
        
        r = n
        res = guess(r)
        if res == 0: return r

        for _ in range(int(math.sqrt(n))):
            rn = (r+l) // 2
            res = guess(rn)
            if res == 0:
                return rn
            elif res < 0:
                r = rn
            else:
                l = rn
