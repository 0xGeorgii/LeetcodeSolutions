class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
       
        i = -1
        for n, tc in enumerate(t):
            if (i := s.find(tc, i+1)) < 0:
                return len(t) - n 
                
        return 0
