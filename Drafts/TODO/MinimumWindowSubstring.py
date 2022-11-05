class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = []
        
        start = -1
        end = 0
        
        tmp = t
        for i,c in enumerate(s):
            if c in tmp:
                if start == -1:
                    start = i
                tmp = tmp.replace(c, "")
            if len(tmp) == 0:
                end = i
                res.append((end-start, s[start:end+1]))
                tmp += s[start]
                for j in range(start+1, len(s)):
                    if s[j] in t:
                        start = j
                        break
                
        res.append((end-start, s[start:end+1]))
        
        print(res)
        return ""
                
def main():
    cases =[
        [ "ADOBECODEBANC", "ABC" ]
    ]
    s = Solution()

    for case in cases:
        r = s.minWindow(case[0], case[1])
        print(r)

if __name__ == "__main__":
    main()
