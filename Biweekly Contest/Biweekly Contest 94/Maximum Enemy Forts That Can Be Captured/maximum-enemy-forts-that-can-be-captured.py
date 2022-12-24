class Solution:
    def captureForts(self, forts: List[int]) -> int:
        
        res = 0
        
        stack = []      
        
        for i in range(len(forts)):
            if forts[i] == 0: continue
            if len(stack) == 0:
                stack.append(i)
                continue
            
            if forts[stack[-1]] != forts[i]:
                n = stack.pop()
                res = max(res, abs(n-i) - 1)

            stack.append(i)
        
        
        return res
