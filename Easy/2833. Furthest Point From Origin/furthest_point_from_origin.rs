use std::cmp;

impl Solution {
    pub fn furthest_distance_from_origin(moves: String) -> i32 {
        
        let cnt_ = moves.matches("_").count();
        let cnt_l = moves.matches("L").count();
        let cnt_r = moves.matches("R").count();

        let res = cnt_ + cmp::max(cnt_l, cnt_r) - cmp::min(cnt_l, cnt_r);
        res as i32

    }
}
