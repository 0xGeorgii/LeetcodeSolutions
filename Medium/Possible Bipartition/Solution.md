# 💡 C++/Python O(n) detailed explained solution

# Intuition
To figure out how to solve this problem it is a good to visualise example test cases first. If you do it, you will notice that the `false` condition appear when a graph has odd-edges cycle.

![Screenshot 2022-12-21 at 6.12.20 PM.png](https://assets.leetcode.com/users/images/b4bebd23-22f3-456f-bfb8-24b8c01fead9_1671628374.3050444.png)

There are two useful wiki pages to read more about this type of problems:
1. [Bipartite graph](https://en.wikipedia.org/wiki/Bipartite_graph)
2. [Graph coloring](https://en.wikipedia.org/wiki/Graph_coloring)

This kind of problems can be solved with a graph coloring approach. The idea is begging from a vertex `x` we color it with a color `a` and color all its children with a color `b`. Then we repear this operation for all vertexes in our graph. If we find an occasion when a color of $$x_i = x(children)_i$$ then this graph is not a bipartial.

# Approach
1. Frstly, we need to build a graph from the finction parameter `dislikes` we have. We build the full graph because we want to observe all edges and be able to reach any vertex starting from any vertex.
2. To track the coloring we have to arrange an array length of `n` to store there an information about colors: $$n[i] = color$$.
3. The default color here is BLUE.
4. We begin from the `0` vertex and to one-by-one checking whether this vertex has a color or not. If not, we coloring it and checking all its children with `dfs` for their colors.
5. If a child verted with the same color is founded then this graph is not bipartial.

## Visualization

`[[1,2],[1,3],[2,4]]` – this graph is shown above (upper-left corner).

* start
![Screenshot 2022-12-21 at 6.27.02 PM.png](https://assets.leetcode.com/users/images/684f7783-a6ff-4e27-85a5-8a3c182681f2_1671629258.3820488.png)
* checking `[1,2]` 
![Screenshot 2022-12-21 at 6.27.58 PM.png](https://assets.leetcode.com/users/images/a6ea51cf-9362-4a8d-a692-3195de517712_1671629395.1232119.png)
* checking `[1,3]` 
![Screenshot 2022-12-21 at 6.28.15 PM.png](https://assets.leetcode.com/users/images/2c6b2a08-3821-4cb7-b46a-010dae6ef34c_1671637097.0901196.png)
* checking `[2,4]` 
![Screenshot 2022-12-21 at 6.28.22 PM.png](https://assets.leetcode.com/users/images/1b21ffaa-864f-4702-a300-0947a297fe79_1671637129.9281485.png)

As we see there are no contradictions. That means this graph is bipartial.

`[[1,2],[2,3],[3,4],[4,5],[1,5]]`  – this graph is shown above (the middle one).

* start 
![Screenshot 2022-12-21 at 8.40.24 PM.png](https://assets.leetcode.com/users/images/ac496092-0fa8-4299-b3a4-2b83b0202fc6_1671637242.103933.png)
* checking `[1,2]` 
![Screenshot 2022-12-21 at 8.41.21 PM.png](https://assets.leetcode.com/users/images/26fda2ad-1f72-42f9-aebd-33dbb85a2cbd_1671637434.5057664.png)
* checking `[2,3]` 
![Screenshot 2022-12-21 at 8.41.33 PM.png](https://assets.leetcode.com/users/images/f361dd65-256a-4007-a3bb-bcf29dd2a0bb_1671637444.0558937.png)
* checking `[3,4]` 
![Screenshot 2022-12-21 at 8.44.49 PM.png](https://assets.leetcode.com/users/images/ef3e7ef2-ac61-4e16-a3ec-041d9a249ed0_1671637500.4675214.png)
* checking `[4,5]` 
![Screenshot 2022-12-21 at 8.42.06 PM.png](https://assets.leetcode.com/users/images/33fd39f3-f0dd-417e-8125-b94bd014d003_1671637471.2012615.png)
* cheking `[1,5]` 
![Screenshot 2022-12-21 at 8.42.27 PM.png](https://assets.leetcode.com/users/images/c02b57a4-468b-4950-a5e9-fa1d7bd331cf_1671637478.8047805.png)

As we see there is a contradiction between the 1st and the 5th vertexes. Hence, this graph is not bipartial.

# Complexity

- Time complexity: O(n)
- Space complexity: O(n)

# Code

## C++

```
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
```

## Python
```
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        m = [0] * n
        blank = 0
        blue = 10e3
        red = -10e3
        graph = defaultdict(list)

        for d in dislikes:
            graph[d[0] - 1].append(d[1] - 1)
            graph[d[1] - 1].append(d[0] - 1)

        def dfs(vertex, color):
            m[vertex] = color
            for v in graph[vertex]:
                if m[v] == color: return False
                if m[v] == blank and not dfs(v, -color):
                    return False
            return True

        
        for i in range(n):
            if m[i] == blank and not dfs(i, blue):
                return False

        return True

```
