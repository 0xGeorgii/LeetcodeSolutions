class Solution {
public:
    int longestPath(vector<int>& parent, string s) {

        map<int, vector<int>> graph;
        for (int i = 1; i < parent.size(); i++) {
            graph[parent[i]].push_back(i);
            graph[i].push_back(parent[i]);
        }

        int res = 0;
        function<int(int, int)> dfs = [&](int node, int parent) {

            bool hasChild = false;
            int maxSubtree = 0;
            for (auto v : graph[node]) {
                if (v > parent) {
                    hasChild = true;
                    int stl = dfs(v, node);
                    if (s[v] == s[node])
                        stl = 0;
                    maxSubtree = max(1, maxSubtree + stl);
                }
            }

            if (!hasChild)
                return 1;
            
            res = max(res, maxSubtree);
            return maxSubtree;
        };

        return dfs(0, -1);
    }
};
