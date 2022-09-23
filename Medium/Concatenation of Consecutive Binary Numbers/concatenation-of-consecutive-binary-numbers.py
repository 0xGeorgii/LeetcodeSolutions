class Solution:
    def concatenatedBinary(self, n: int) -> int:        
        res = ""        
        for i in range(n):
            res += f"{bin(i+1)[2:]}"
            
        return int(res, 2) % (10 ** 9 + 7)
