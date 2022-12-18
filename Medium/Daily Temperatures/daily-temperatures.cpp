class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        stack<tuple<int, int>> stack;

        for (int i = 0; i < temperatures.size(); ++i)
        {
            int t = temperatures[i];

            if (stack.size() == 0)
            {
                stack.push(make_tuple(i, t));
                continue;
            }

            if (get<1>(stack.top()) > t)
                stack.push(make_tuple(i, t));
            else
            {
                while (!stack.empty() && get<1>(stack.top()) < t)
                {
                    int ix = get<0>(stack.top());
                    stack.pop();
                    res[ix] = i - ix;
                }
                stack.push(make_tuple(i, t));
            }
        }

        return res;
    }
};
