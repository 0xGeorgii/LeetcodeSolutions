class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        if sentence[0] != sentence[-1]:
            return False
        
        ss = sentence.split()
        
        for i in range(len(ss) - 1):
            s1 = ss[i]
            s2 = ss[i+1]
            
            if s1[-1] != s2[0]:
                return False
            
        return True
