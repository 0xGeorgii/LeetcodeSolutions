class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        len1 = ax2 - ax1
        wid1 = ay2 - ay1
        area1 = len1 * wid1 
        
        len2 = bx2 - bx1
        wid2 = by2 - by1
        area2 = len2 * wid2

        len3 = min(ax2, bx2) - max(ax1, bx1)
        wid3 = min(ay2, by2) - max(ay1, by1)
        area3 = len3 * wid3 if len3 > 0 and wid3 > 0 else 0

        return int(area1 + area2 - area3)
