class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) return std::max(nums[0], nums[1]);
        int res = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            std::vector<int> dp(nums.size(), 0);
            for (int j = i; j < nums.size(); ++j)
            {
                int l = (j-2) < 0 ? 0 : dp[j-2];
                int r = (j-1) < 0 ? 0 : dp[j-1];
                dp[j] = max(l + nums[j], r);
            }

            res = std::max(res, dp[nums.size() - 1]);
        }
        return res;
    }
};
