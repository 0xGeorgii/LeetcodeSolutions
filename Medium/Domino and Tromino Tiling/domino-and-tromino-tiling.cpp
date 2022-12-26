class Solution {
public:
    int numTilings(int n) {
        
        if (n == 1 || n == 2) return n;

        vector<long> dp (n, 0);
        dp[0] = 1;
        dp[1] = 2;
        dp[2] = 5;

        const long MOD = 1000000007;
        for (int i = 3; i < n; ++i)
            dp[i] = (dp[i-1] * 2  % MOD) + dp[i-3];

        return dp[n-1] % MOD;
    }
};
