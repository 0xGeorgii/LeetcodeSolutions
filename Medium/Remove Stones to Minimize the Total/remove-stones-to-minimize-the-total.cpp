class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        make_heap(piles.begin(), piles.end());
        for (int i = 0; i < k; ++i) {
            for (auto i : piles) std::cout << i << " ";
            cout << endl;
            int n = piles.front();
            cout << n << endl;
            pop_heap(piles.begin(), piles.end());
            //piles.pop_back();
            n = ceil(n / 2);
            piles.push_back(n);
            push_heap(piles.begin(), piles.end());
            for (auto i : piles) std::cout << i << " ";
        }
        return std::reduce(piles.begin(), piles.end());
    }
};
