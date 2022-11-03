class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        if len(words) == 1:
            return 2 if words[0][0] == words[0][1] else 0
        
        data = Counter(words)
        acc = 0
        central = False
        
        for k, v in data.items():
            
            k1 = k[1] + k[0]
            
            if k == k1:
                if v % 2 == 0:
                    acc += v
                else:
                    acc += v - 1
                    central = True

            elif k1 in data:
                n = min(v, data[k1])
                acc += n
        
        if central:
            acc += 1
        
        return acc * 2
