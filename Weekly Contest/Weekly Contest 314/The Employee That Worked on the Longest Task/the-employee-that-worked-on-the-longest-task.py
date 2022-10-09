class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        
        res = []
        
        res.append(
            (logs[0][1] - 0, logs[0][0])
        )
        
        for i in range(len(logs) - 1):
            
            time = logs[i+1][1] - logs[i][1]
            id = logs[i+1][0]
            
            res.append(
                (time, id)
            )
        
        res = sorted(res, key=lambda x: (-x[0], x[1]))
        
        return res[0][1]
