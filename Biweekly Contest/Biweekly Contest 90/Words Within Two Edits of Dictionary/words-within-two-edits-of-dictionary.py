class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        res = []
        
        for q in queries:
                                    
            for d in dictionary:
                mistakes = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        mistakes +=  1                        
                        if mistakes > 2:
                            break
                            
                if mistakes <= 2:
                    res.append(q)
                    break
        
        return res
