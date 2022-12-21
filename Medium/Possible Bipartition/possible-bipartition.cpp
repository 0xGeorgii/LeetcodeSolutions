class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        const int BLANK = 0;
        const int BLUE = 10e4;
        const int RED = -10e4;

        vector<int> m(n, BLANK);
        map<int, vector<int>> graph;

        for (auto d : dislikes)
        {
            int k = d[0] - 1;
            int v = d[1] - 1;
            graph[k].emplace_back(v);
            graph[v].emplace_back(k);
        }

        function<bool(int, int)> dfs = [&](int vertex, int color)
        {
            m[vertex] = color;

            for (auto v : graph[vertex])
            {
                if (m[v] == color) return false;
                if (m[v] == BLANK && !dfs(v, -color))
                    return false;
            }
            return true;
        };

        for (int i = 0; i < n; ++i)
        {
            if (m[i] == BLANK && !dfs(i, BLUE))
                return false;
        }

        return true;
    }
};
