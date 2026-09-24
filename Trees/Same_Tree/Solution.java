package Trees.Same_Tree;

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
       public boolean isSameTree(TreeNode p, TreeNode q) {
           if( p == null && q == null ){
               return true ; 
           }else if( p == null || q == null ){
               return false ; 
           }else {
               return p.val == q.val && isSameTree( p.right,q.right ) && isSameTree(p.left,q.left) ; 
           }
       }
   }