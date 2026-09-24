package Trees.Balanced_Binary_Tree;


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
    
   public int isValid( TreeNode root ){
       if( root == null ){
           return 0 ; 
       }
       int a = isValid( root.right ) ; 
       int b = isValid( root.left ) ; 
       if( a != -1 && b != -1 && Math.abs(a-b)<=1 ){
           return Math.max( a , b ) + 1 ;
       }
       return -1 ; 
   }
   public boolean isBalanced(TreeNode root) {
       if( root == null ){
           return true ; 
       }
       if( isValid( root ) != -1 ){
           return true ; 
       } 
       return false ; 
   }
}