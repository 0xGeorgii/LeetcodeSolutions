class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        if len(fruits) < 3:
            return len(fruits)

        res = -inf
        q = deque([])
        m = defaultdict(int)

        for f in fruits:

            if len(m) == 2 and f not in m:
                res = max(res, sum(m.values()))
                while len(m) > 1:
                    n = q.popleft()
                    m[n] -= 1
                    if m[n] == 0:
                        del m[n]
                
            q.append(f)
            m[f] += 1

        res = max(res, sum(m.values()))
        return res
