class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        
        uint sum = 0;
        stack<TreeNode*> stack;
        stack.push(root);

        while(!stack.empty())
        {
            auto node = stack.top();
            stack.pop();

            if(node->val >= low && node->val <= high)
                sum += node->val;

            if(node->left != nullptr) stack.push(node->left);
            if(node->right != nullptr) stack.push(node->right);
        }

        return sum;
    }
};
