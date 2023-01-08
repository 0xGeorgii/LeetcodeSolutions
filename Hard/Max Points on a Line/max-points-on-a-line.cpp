class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        if (points.size() == 1) return 1;
        int res = -100000;
        for (int i = 0; i < points.size(); ++i) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            map<double, int> map;
            for (int j = 0; j < points.size(); ++j) {

                if (i == j) continue;
                int x2 = points[j][0];
                int y2 = points[j][1];

                double slope = atan2(y2 - y1, x2 - x1);
                map[slope] += 1;
            }

            int max = -100000;
            for (auto [k, v] : map) {
                max = std::max(max, v);
            }
            res = std::max(res, max);
        }

        return res + 1;
    }
};
