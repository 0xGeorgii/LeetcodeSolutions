class Solution:
    
    @lru_cache
    def pivotInteger(self, n: int) -> int:
        
        if n == 1: return 1
        
        x = n-1
        
        while x > 0:
            
            r1, r2 = 0, 0
            
            for i in range(1, x+1):
                r1 += i
            
            for i in range(x, n+1):
                r2 += i
                
            if r1 == r2:
                return x
            
            x -= 1
            
            
        return -1
