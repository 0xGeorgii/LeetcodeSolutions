class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        
        map<int, vector<int>> graph;

        for (auto edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        function<int(int, int)> dfs = [&](int node, int parent) {
            int res = 0;

            for (auto v : graph[node])
                if (v != parent)
                    res += dfs(v, node);
            
            if (res > 0 || hasApple[node])
                return res + 2;

            return res;
        };

        return max(0, dfs(0, -1) - 2);
    }
};
