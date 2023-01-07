class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total_cost = sum(cost)
        data = []
        for i in range(len(gas)):
            data.append((gas[i] - cost[i], i))
        mv = data[0][0]
        
        for p, i in sorted(data, key=lambda x: (-x[0], x[1])):
            acc = 0
            for j in range(i, i + len(data)):
                n = j % len(data)
                acc += data[n][0]
                if acc < 0:
                    break
            else:
                return i

        return -1
