class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        map<int, vector<int>> map;
        vector<int> qry = queries;
        sort(qry.begin(), qry.end());

        for (int i = 0; i < qry.size(); ++i) {
            int pos = i > 0 ? map[qry[i-1]][0] : 0;
            int ans = i > 0 ? map[qry[i-1]][1] : 0;

            for (; pos < nums.size(); ++pos) {
                if ( ans + nums[pos] > qry[i] ) {
                    map.insert({ qry[i], { pos, ans } });
                    break;
                }
                else
                    ans += nums[pos];
            }

            if (map.find(qry[i]) == map.end())
                map.insert({ qry[i], { (int) nums.size(), ans } });
        }

        vector<int> res;
        for (auto& q : queries)
            res.push_back(map[q][0]);

        return res;
    }
};
