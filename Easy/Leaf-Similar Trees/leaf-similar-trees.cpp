class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        
        auto traverse_tree = [](TreeNode* root, vector<uint>* output)
        {
            stack<TreeNode*> stack;
            stack.push(root);

            while (!stack.empty())
            {
                auto n = stack.top();
                stack.pop();

                if (n->left != nullptr) stack.push(n->left);
                if (n->right != nullptr) stack.push(n->right);
                if (n->left == nullptr and n->right == nullptr) output->emplace_back(n->val);
            }
        };

        vector<uint> res1;
        vector<uint> res2;
        traverse_tree(root1, &res1);
        traverse_tree(root2, &res2);
        return res1 == res2;
    }
};
