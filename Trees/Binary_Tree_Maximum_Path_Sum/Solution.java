package Trees.Binary_Tree_Maximum_Path_Sum;
\
class Solution {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    int rs = 0 ; 
    public int helper( TreeNode root ){
        if( root == null ){
            return 0 ;
        }
        int maxRight = Math.max( 0 ,  helper( root.right ) ) ; 
        int maxLeft = Math.max( 0 ,  helper( root.left ) ) ; 
        rs = Math.max( rs , root.val + maxLeft + maxRight ) ; 
        return root.val + Math.max( maxLeft , maxRight ) ; 
    }
    public int maxPathSum(TreeNode root) {
        this.rs = root.val ; 
        helper( root ) ; 
        return rs ; 
    }
}