class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        
        l1 = len(cnt1)
        l2 = len(cnt2)
        
        if len(word1) == len(word2) and l1 == l2:
            return True
        
        def copy(src):
            res = {}
            
            for k, v in src.items():
                res[k] = v
            
            return res

        for k1, v1 in cnt1.items():
            for k2, v2 in cnt2.items():            
                
                t1 = copy(cnt1)
                t1v = v1
                if v1 == 1:
                    del t1[k1]
                else:
                    t1v -= 1
                    
                t2 = copy(cnt2)
                if v2 == 1:
                    del t2[k2]
                else:
                    v2 -= 1


                if k2 in t1: t1[k2] += 1
                else: t1[k2] = 1
                if k1 in t2: t2[k1] += 1
                else: t2[k1] = 1
                
                if len(t1) == len(t2):
                    return True
        
        return False
