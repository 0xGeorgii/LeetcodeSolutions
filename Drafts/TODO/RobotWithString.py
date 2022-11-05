class Solution:
    def robotWithString(self, s: str) -> str:
        
        res = ""        
        t = []
        
        for i in range(len(s)-1):
            if s[i] >= s[i+1]:
                t.append(s[i])
            else:
                while len(t) > 0:
                    res += t.pop()
        else:
            while len(t) > 0:
                res += t.pop()
        
        if len(s) - len(res) > 0:
            pass
        
        return res

def main():
    cases = [
        "zza"
    ]

    s = Solution()

    for case in cases:
        print(s.robotWithString(case))

if __name__ == "__main__":
    main()
