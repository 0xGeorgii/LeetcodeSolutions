class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        res = []
        
        res.append(pref[0])
        acc = pref[0]
        
        for i in range(1, len(pref)):
            
            if pref[i] == 0:
                res.append(acc)
                acc = acc ^ acc
            else:
                x = acc ^ pref[i]
                acc = acc ^ x
                res.append(x)
                    
        return res
