class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        ladder = zip(efficiency, speed)
        ladder = sorted(ladder, key=lambda x: (-x[0], x[1]))
        team = []       
        max_performance = -float("inf")
        sum_s = 0
            
        for i in range(len(ladder)):
            en = ladder[i]
            sum_s += en[1]
            heappush(team, en[1])
            
            if len(team) > k:
                min_s = heappop(team)
                sum_s -= min_s
    
            max_performance = max(max_performance, sum_s * en[0])
            
        return max_performance % (10 ** 9 + 7)
