class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        q = deque(nums)
        res = 0
        
        while q:
            if len(q) > 1:
                x = q.popleft()
                y = q.pop()                
                s = str(x) + str(y)
                res += int(s)
            else:
                x = q.pop()
                res += int(x)
        
        return res
