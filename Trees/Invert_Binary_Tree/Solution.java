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
    public void invert( TreeNode root ){
        if( root == null ){
            return  ; 
        }
        TreeNode temp = root.right ; 
        root.right = root.left ; 
        root.left = temp ; 
        invert( root.right ) ; 
        invert( root.left ) ; 
    }
    public TreeNode invertTree(TreeNode root) {
        invert( root ) ; 
        return root ; 
    }
}