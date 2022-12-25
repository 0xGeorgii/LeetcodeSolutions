class Solution {
public:
    vector<vector<int>> mergeSimilarItems(vector<vector<int>>& items1, vector<vector<int>>& items2) {
        map<int, int> m1;
        map<int, int> m2;
        set<int> keys;

        for_each(items1.begin(), items1.end(), [&](vector<int> item){
            m1.insert({item[0], item[1]});
            keys.insert(item[0]);
        });

        for_each(items2.begin(), items2.end(), [&](vector<int> item){
            m2.insert({item[0], item[1]});
            keys.insert(item[0]);
        });

        vector<vector<int>> res;
        for (auto& key : keys) {
            int acc = 0;

            if (m1.find(key) != m1.end())
                acc += m1[key];
            
            if (m2.find(key) != m2.end())
                acc += m2[key];
            
            res.push_back({ key, acc });
        }

        return res;
    }
};
