class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        if target not in words: return -1
        
        n = len(words)
        res = inf
        steps = 0
        
        while True:
            wl = words[(startIndex + steps) % n]
            wr = words[(startIndex - steps + n) % n]
            if target in [ wl, wr ]:
                return steps
            steps += 1
            
        return res
