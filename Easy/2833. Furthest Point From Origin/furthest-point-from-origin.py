class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        cnt_ = moves.count("_")
        cnt_l = moves.count("L")
        cnt_r = moves.count("R")
        
        return cnt_ + max(cnt_l, cnt_r) - min(cnt_l, cnt_r)
