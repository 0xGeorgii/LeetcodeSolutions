class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = ""
        tmp_res = ""
        
        i = 0
        
        while i < len(s):
            ch = s[i]
            i += 1
            
            if len(tmp_res) == 0:
                tmp_res += ch
                continue

            if ord(ch) == ord(tmp_res[-1])+1:
                tmp_res += ch
            else:
                i -= 1
                if len(tmp_res) > len(res):
                    res = tmp_res
                tmp_res = ""
                    
        
        return max(len(res), len(tmp_res))
