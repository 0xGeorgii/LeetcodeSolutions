class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        m = []
        
        for r in score:
            m.append( (r[k], r) )
            
        m.sort(reverse=True)
        res = []
        
        for r in m:
            res.append(r[1])
        
        return res
