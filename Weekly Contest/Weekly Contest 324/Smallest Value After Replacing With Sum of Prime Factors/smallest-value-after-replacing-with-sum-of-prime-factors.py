class Solution:
    
    def smallestValue(self, n: int) -> int:

        @lru_cache    
        def get_p_factors_sum(x):
            res = 0
            i = 2
            while x > 1:
                if x % i == 0:
                    res += i
                    x = x / i
                else:
                    i += 1
            return res
                    
        sv = get_p_factors_sum(n)
        while True:
            nv = get_p_factors_sum(sv)
            if sv > nv:
                sv = nv
            else:
                return nv
