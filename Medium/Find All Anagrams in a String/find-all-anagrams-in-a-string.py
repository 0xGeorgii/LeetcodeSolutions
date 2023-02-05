class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        cnt = Counter(p)
        d = defaultdict(int)
        q = deque([])
        pl = len(p)
        res = []

        for i, c in enumerate(s):
            q.append(c)
            d[c] += 1

            if len(q) == pl:
                if d == cnt:
                    res.append(i - pl + 1)
                n = q.popleft()
                d[n] -= 1
                if d[n] == 0:
                    del d[n]

        return res
