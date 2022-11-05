import math
import re
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        powers = [1]
        
        while sum(powers) < n:
            s = math.floor(math.sqrt(n))
            x = pow(2, s)
            n -= x
            powers.append(x)
        
        powers.sort()
        print(powers)
        
        res = []
        x = 0
        
        for qry in queries:
            k = 1
            i = qry[0]

            while True:
                k = k * powers[i - 1]
                i += 1
                if i > qry[1]:
                    break
            res.append(k)
            
        return res

def main():
    cases = [
        [
            13,
            [[1,2],[1,1]]
        ]
    ]

    s = Solution()

    for case in cases:
        print(s.productQueries(case[0], case[1]))

if __name__ == "__main__":
    main()
