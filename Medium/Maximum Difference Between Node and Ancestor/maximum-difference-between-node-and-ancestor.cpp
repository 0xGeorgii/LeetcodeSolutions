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
    int maxAncestorDiff(TreeNode* root) {

        std::function<int(TreeNode*, int, int)> search = [&](TreeNode* node, int min, int max)
        {
            if (node == nullptr) return max - min;

            min = std::min(node->val, min);
            max = std::max(node->val, max);

            int l = search(node->left, min, max);
            int r = search(node->right, min, max);

            return std::max(l, r);
        };

        return search(root, root->val, root->val);        
    }
};
