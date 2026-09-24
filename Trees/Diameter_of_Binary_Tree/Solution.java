package Trees.Diameter_of_Binary_Tree;

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
   public int getHeight( TreeNode node ){
       if( node  == null ){
           return 0 ;
       }
       int l = getHeight( node.left ) ; 
       int r = getHeight( node.right ) ; 
       rs = Math.max( rs , l+r ) ; 
       return Math.max( l , r ) + 1 ;
   }
   public int diameterOfBinaryTree(TreeNode root) {
       getHeight( root ) ; 
       return rs ; 
   }
}