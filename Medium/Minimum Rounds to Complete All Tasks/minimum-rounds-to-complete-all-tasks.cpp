class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        map<int, int> map;
        for (int t : tasks) ++map[t];
        int res = 0;
        for (auto [k, v] : map) {
            if (v == 1) return -1;
            res += (v + 2) / 3;
        }
        return res;
    }
};
