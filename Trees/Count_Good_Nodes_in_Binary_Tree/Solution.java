package Trees.Count_Good_Nodes_in_Binary_Tree;

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
    public void dfs( TreeNode root , int curr ){
        if( root == null ){
            return ; 
        }
        if( root.val >= curr ){
            rs++ ; 
        }
        curr = Math.max( curr , root.val ) ;
        dfs( root.left , curr ) ; 
        dfs( root.right , curr ) ; 
    }
    public int goodNodes(TreeNode root) {
        dfs( root , root.val ) ; 
        return rs ; 
    }
}