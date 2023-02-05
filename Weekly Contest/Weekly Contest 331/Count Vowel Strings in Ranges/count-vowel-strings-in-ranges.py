class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vs = []
        intervals = {}
        acc = 0
        
        for i, w in enumerate(words):
            if w[0] in ['a', 'e', 'i', 'o', 'u'] and w[-1] in ['a', 'e', 'i', 'o', 'u']:
                vs.append(1)
                acc += 1
            else:
                vs.append(0)
            
            intervals[(0, i)] = acc
            
        print(intervals)                        
        res = []
        
        for q in queries:
            t = (q[0], q[1])
            if t in intervals:
                res.append(intervals[t])
            else:
                interval = intervals[(0, q[1])]
                n = interval - intervals[(0, q[0]-1)]
                res.append(n)
    
        return res
