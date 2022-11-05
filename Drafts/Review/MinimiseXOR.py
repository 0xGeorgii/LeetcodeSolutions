from cgitb import reset
from itertools import groupby
import itertools
from typing import List

#TODO: https://leetcode.com/contest/weekly-contest-313/ranking/
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        def snoob(x):
     
            next = 0
            if(x):
                
                rightOne = x & -(x)
                
                nextHigherOneBit = x + int(rightOne)
                
                rightOnesPattern = x ^ int(nextHigherOneBit)
                
                rightOnesPattern = (int(rightOnesPattern) /
                                    int(rightOne))
                
                rightOnesPattern = int(rightOnesPattern) >> 2
                
                next = nextHigherOneBit | rightOnesPattern
            return next
        
        bits = bin(num2)[2:].replace("0", "")
        res, min = 0, float("inf")
        n = int(bits, 2)
        
        for _ in range(64-len(bits)):         
            n1 = n ^ num1
            if n1 < min:
                min = n1
                res = n
            n = snoob(n)

        return res

def main():
    solution = Solution()
    cases = [
        [ 3, 5 , 3],
        [ 1, 12, 3],
        [ 25, 72, 24],
        [ 91, 18, 80],
        [ 5848, 2308, 5632]
    ]
    for case in cases:
        res = solution.minimizeXor(case[0], case[1])
        print(f"out: {res} exp: {case[2]} -> {res == case[2]}")

if __name__ == "__main__":
    main()
