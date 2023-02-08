class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        seen = set([start])
        q = deque([start])
        while q:
            i = q.popleft()
            seen.add(i)

            if arr[i] == 0:
                return True
            
            l = i - arr[i]
            if l >= 0 and l not in seen:
                q.append(l)
            
            r = i + arr[i]
            if r < len(arr) and r not in seen:
                q.append(r)

        return False
