class Solution:
    def allPathsSourceTarget(self, vxs: List[List[int]]) -> List[List[int]]:

        def dfs(i, visited):
            nonlocal res
            if i == len(vxs) - 1:
                res.append(visited + [i])
                return

            for v in vxs[i]:
                if v in visited: continue
                dfs(v, visited + [i])

        res = []
        dfs(0, [])

        return res
