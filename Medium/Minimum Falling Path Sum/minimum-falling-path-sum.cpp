class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {

        int ms = matrix[0].size();

        for(int i = 1; i < ms; ++i)
        {
            for(int j = 0; j < ms; ++j)
            {
                int a = matrix[i-1][j];
                int b = matrix[i-1][max(0, j - 1)];
                int c = matrix[i-1][min(ms - 1, j + 1)];

                matrix[i][j] += min(a, min(b, c));
            }
        }
        
        return *min_element(
            matrix[ms - 1].begin(),
            matrix[ms - 1].end()
        );
    }
};
