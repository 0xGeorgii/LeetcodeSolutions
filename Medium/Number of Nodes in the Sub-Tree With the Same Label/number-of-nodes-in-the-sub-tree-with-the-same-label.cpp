class Solution {
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {

        vector<int> res (n, 0);
        map<int, vector<int>> graph;
        for (auto v : edges) {
            graph[v[0]].push_back(v[1]);
            graph[v[1]].push_back(v[0]);
        }

        function<vector<int>(int, int)> dfs = [&](int vertex, int parent) {
            vector<int> v(26, 0);
            int i = labels[vertex] - 97;
            ++v[i];
            for (auto vx : graph[vertex]) {
                if (vx != parent) {
                    auto dv = dfs(vx, vertex);
                    for (int j = 0; j < dv.size(); ++j)
                        v[j] += dv[j];
                }
            }
            res[vertex] = v[i];
            return v;
        };

        dfs(0,-1);
        return res;
    }
};
