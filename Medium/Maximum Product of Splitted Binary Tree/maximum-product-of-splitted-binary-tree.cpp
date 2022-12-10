class Solution {
public:
    int maxProduct(TreeNode* root) {

        long total = 0;
        std::vector<long> subtrees;

        std::function<long(TreeNode*)> search = [&](TreeNode* node)
        {
            if (node == nullptr) return static_cast<long>(0);

            total += node->val;

            long subtotal = node->val;
            subtotal += search(node->left);
            subtotal += search(node->right);
            subtrees.emplace_back(subtotal);

            return subtotal;
        };

        search(root);

        long max = 0;
        for (auto st : subtrees)
            max = std::max(max, (total-st) * st );

        return max % static_cast<long>(1e9+7);
    }
};
