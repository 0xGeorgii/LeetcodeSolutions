class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in range(len(distance)):
            c = chr(97 + i)
            if c not in s:
                continue
            index1 = s.index(c)
            index2 = index1 + distance[i] + 1
            if index2 >= len(s):
                return False
            if s[index2] != c:
                return False
            
        return True
            
