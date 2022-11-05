from re import M
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        def convolute_maxtrixes(m1, m2):
            acc = 0            
            for r in range(len(m1)):
                for c in range(len(m1)):
                    acc +=  m1[r][c] * m2[r][c]            
            return acc
        
        
        ml = len(img1[0])
        res = convolute_maxtrixes(img1, img2)
        mml = ml + ((ml-1) * 2)

        mm = [ [0] * mml for _ in range(mml)]

        for i in range(mml):
            for j in range(mml):
                m = [ [0] * ml for _ in range(ml) ]

                for x in range(ml):
                    for y in range(ml):
                        x -= ml - 1
                        y -= ml - 1

                        if ml > x > 0 and ml > y > 0:
                            m[x][y] = img1[x][y]
                
                res = max(res, convolute_maxtrixes(m, img2))

        
        return res

def main():

    cases = [
        [
            [[1,1,0],[0,1,0],[0,1,0]],
            [[0,0,0],[0,1,1],[0,0,1]]
        ]
    ]

    s = Solution()

    for case in cases:
        res = s.largestOverlap(case[0], case[1])
        print(res)

if __name__ == "__main__":
    main()
