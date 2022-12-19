class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int src, int dst) {
        if(src == dst) return true;

        vector<unordered_set<int>> graph(n);
        for(auto edge : edges)
        {
            graph[edge[0]].insert(edge[1]);
            graph[edge[1]].insert(edge[0]);
        }

        set<int> seen;
        queue<int> nodes;
        nodes.push(src);

        while(!nodes.empty())
        {
            queue<int> tmp;
            while(!nodes.empty())
            {
                int node = nodes.front();
                nodes.pop();
                for(auto x : graph[node])
                {
                    if(seen.find(x) == seen.end())
                    {
                        if(x == dst) return true;
                        seen.insert(x);
                        tmp.push(x);
                    }
                }
            }
            nodes = tmp;
        }

        return false;
    }
};
