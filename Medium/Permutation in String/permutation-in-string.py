class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d1 = Counter(s1)
        has_candidate = False
        
        q = deque([])
        qd = defaultdict(int)

        for i in range(len(s2)):
            c = s2[i]

            if c in d1:
                has_candidate = True
                q.append(c)
                qd[c] += 1

                if qd[c] > d1[c]:
                    while q:
                        cc = q.popleft()
                        qd[cc] -= 1
                        if cc == c: break

                if d1 == qd:
                    return True    
            else:
                q = deque([])
                qd = defaultdict(int)

        if has_candidate:
            return d1 == qd

        return False
