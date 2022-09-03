/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int GoodNodes(TreeNode root) {
        
        var res = 1;
        var nodes = new Stack<Tuple<TreeNode, int>>();
        nodes.Push(new Tuple<TreeNode, int>(root, root.val));
                
        while(nodes.Count() > 0)
        {
            var node = nodes.Pop();
            var treeNode = node.Item1;
            var maxVal = node.Item2;
            if (treeNode.left != null)
            {
                if(maxVal <= treeNode.left.val)
                {
                    res++;                    
                }
                nodes.Push(
                    new
                    (
                        treeNode.left,
                        Math.Max(maxVal, treeNode.left.val)
                    ));
            }
            if (treeNode.right != null)
            {
                if(maxVal <= treeNode.right.val)
                {
                    res++;                    
                }
                nodes.Push(
                    new
                    (
                        treeNode.right,
                        Math.Max(maxVal, treeNode.right.val)
                    ));
            }
        }    
        return res;    
    }
}
