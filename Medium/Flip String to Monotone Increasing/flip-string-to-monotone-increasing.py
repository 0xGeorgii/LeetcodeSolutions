class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        if len(s) == 1: return 0

        cnt_0 = s.count('0')
        cnt_1 = len(s) - cnt_0

        left_0 = 0
        left_1 = 0

        res = min(cnt_0, cnt_1)

        for i in range(len(s)):

            if s[i] == '0':
                left_0 += 1
            else:
                left_1 += 1

            right_0 = cnt_0 - left_0
            
            res = min(res, left_1 + right_0)

        return res
