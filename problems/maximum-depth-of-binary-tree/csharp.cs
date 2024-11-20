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
    // Solution is to use DFS
    public int MaxDepth(TreeNode root) {
        if (root is null) return 0;
        
        var leftHeight = 1 + MaxDepth(root.left);
        var rightHeight = 1 + MaxDepth(root.right);

        return Math.Max(leftHeight, rightHeight);
    }
}