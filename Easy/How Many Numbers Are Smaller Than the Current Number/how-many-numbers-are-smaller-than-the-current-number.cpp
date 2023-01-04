class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {

        vector<int> order = nums;
        sort(order.begin(), order.end());
        vector<int> res;

        for (int i : nums) {
            int index = find(order.begin(), order.end(), i) - order.begin();
            res.push_back(index);
        }
        
        return res;
    }
};
