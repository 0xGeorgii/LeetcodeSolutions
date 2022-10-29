class Solution:
    def countTime(self, time: str) -> int:
        q = len([i for i, c in enumerate(time) if c == "?"])
                
        ans = 0
        
        r = "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
        
        
        if q == 0:
            return 1
        elif q == 1:
            for i in range(10):
                tmp = time.replace("?", str(i), 1)
                if re.search(r, tmp) is not None:
                    ans += 1
        elif q == 2:
            for i in range(10):
                for j in range(10):
                    tmp = time.replace("?", str(i), 1)
                    tmp = tmp.replace("?", str(j), 1)
                    if re.search(r, tmp) is not None:
                        ans += 1
        elif q == 3:
            for i in range(10):
                for j in range(10):
                    for k in range(10):
                        tmp = time.replace("?", str(i), 1)
                        tmp = tmp.replace("?", str(j), 1)
                        tmp = tmp.replace("?", str(k), 1)
                        if re.search(r, tmp) is not None:
                            ans += 1
        elif q == 4:
            for i in range(10):
                for j in range(10):
                    for k in range(10):
                        for n in range(10):
                            tmp = time.replace("?", str(i), 1)
                            tmp = tmp.replace("?", str(j), 1)
                            tmp = tmp.replace("?", str(k), 1)
                            tmp = tmp.replace("?", str(n), 1)
                            if re.search(r, tmp) is not None:
                                ans += 1
        
        return ans
