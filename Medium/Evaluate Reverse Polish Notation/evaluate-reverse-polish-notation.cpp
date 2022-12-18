class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        vector<string> valid_ops = { "+", "-", "*", "/" };
        map<string, std::function<long(long,long)>> ops;
        ops.emplace("+", [=](long a, long b) { return a + b; });
        ops.emplace("-", [=](long a, long b) { return a - b; });
        ops.emplace("*", [=](long a, long b) { return a * b; });
        ops.emplace("/", [=](long a, long b) { return a / b; });

        stack<int> stack;

        for (auto t : tokens)
        {
            if (find(valid_ops.begin(), valid_ops.end(), t) != valid_ops.end())
            {
                int a = stack.top();
                stack.pop();
                int b = stack.top();
                stack.pop();
                stack.push(ops[t](b, a));
            }
            else
            {
                stack.push(stoi(t));
            }
        }

        return stack.top();
    }
};
