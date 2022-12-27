class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        diff = [ capacity[i] - rocks[i] for i in range(len(capacity)) ]
        diff.sort()

        res = 0

        for i in range(len(diff)):
            if diff[i] == 0:
                res += 1
                continue
            additionalRocks -= diff[i]
            if additionalRocks >= 0:
                res += 1
        
        return res
