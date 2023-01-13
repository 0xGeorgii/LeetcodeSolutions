class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int res = 0;
        for (auto word : words)
            if (word.rfind(pref, 0) == 0) res += 1;
        return res;
    }
};
