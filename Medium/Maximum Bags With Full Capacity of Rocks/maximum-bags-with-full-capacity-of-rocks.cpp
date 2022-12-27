class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, long additionalRocks) {
        vector<int> diff;

        for (int i = 0; i < capacity.size(); ++i)
            diff.emplace_back(capacity[i] - rocks[i]);
        
        sort(diff.begin(), diff.end());
        int res = 0;

        for (auto i : diff) {
            if (i == 0) {
                res += 1;
                continue;
            }
            additionalRocks -= i;
            if (additionalRocks >= 0)
                res += 1;
        }

        return res;
    }
};
