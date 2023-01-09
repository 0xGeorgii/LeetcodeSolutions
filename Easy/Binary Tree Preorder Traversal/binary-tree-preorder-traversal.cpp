/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {

        if (!root) return {};
        if (!root->left && !root->right) return { root->val };

        vector<int> res;
        set<TreeNode*> set;
        stack<TreeNode*> stack;
        stack.push(root);

        while (!stack.empty()) {
            auto node = stack.top();
            stack.pop();

            if (find(set.begin(), set.end(), node) == set.end())
            res.push_back(node->val);
            set.insert(node);

            if (!node->left && !node->right)
                continue;

            if (node->left && find(set.begin(), set.end(), node->left) == set.end()) {
                stack.push(node);
                stack.push(node->left);
                continue;
            }

            if (node->right && find(set.begin(), set.end(), node->right) == set.end()) {
                stack.push(node->right);
                continue;
            }
        }

        return res;
    }
};
