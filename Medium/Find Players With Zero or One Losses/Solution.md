# 💡Python O(n) simple solution

# Intuition
If you need to aggregate and count some sequens you cen use either array or hasmap if it is a matter of a uniqueness.

# Approach
In our case we need to find unique teams that either not loose or loose not more than 1 match. So we need to distribute the information about all matches among two grous and
1. Check for intesection for winners
2. Check for 1 lost for loosers

# Complexity
- Time complexity: O(n)
- Space complexity: O(n)

# Code
```
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winners, losers = defaultdict(int), defaultdict(int)

        for match in matches:

            winners[match[0]] += 1
            losers[match[1]] += 1

        res_1, res_2 = [], []

        for k, v in winners.items():
            if k not in losers:
                res_1.append(k)
        
        for k, v in losers.items():
            if v == 1:
                res_2.append(k)

        res_1.sort()
        res_2.sort()
        
        return [ res_1, res_2 ]
```
