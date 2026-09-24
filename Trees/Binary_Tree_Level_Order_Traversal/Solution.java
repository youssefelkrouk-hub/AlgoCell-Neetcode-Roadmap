package Trees.Binary_Tree_Level_Order_Traversal;

import java.util.*;

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
   
       public List<List<Integer>> levelOrder(TreeNode root) {
           List<List<Integer>> rs = new ArrayList<>() ; 
           if( root == null ){
               return rs ;
           }
           Queue<TreeNode> q = new LinkedList<>() ; 
           q.add( root ) ; 
           while( !q.isEmpty() ){
               List<Integer> curr = new ArrayList<>() ; 
               int len = q.size() ; 
               while( len-- > 0 ){
                   TreeNode node = q.poll() ; 
                   curr.add( node.val ) ;
                   if( node.left != null ){
                       q.add( node.left ) ; 
                   }
                   if( node.right != null ){
                       q.add( node.right ) ; 
                   }
               }
               rs.add( curr ) ; 
           }
           return rs ; 
       }
   }