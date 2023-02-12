class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        
        res = []
        
        @lru_cache
        def find_in_s(ss):
            try:
                return s.index(ss)
            except:
                return -1
        
        for q in queries:
            n = q[0] ^ q[1]            
            n = bin(n)[2:]
            i = find_in_s(n)
            if i == -1:
                res.append([-1, -1])
            else:
                res.append([i, i + len(n) - 1])
                            
        
        return res
