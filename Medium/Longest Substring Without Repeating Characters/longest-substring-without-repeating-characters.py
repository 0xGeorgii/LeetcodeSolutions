class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0: return 0

        m, q, res = set(), deque([]), 0
        
        for c in s:

            if c not in m:
                m.add(c)
                q.append(c)
            else:
                res = max(res, len(q))
                while c in m:
                    n = q.popleft()
                    m.remove(n)
                m.add(c)
                q.append(c)

        res = max(res, len(m))

        return res
