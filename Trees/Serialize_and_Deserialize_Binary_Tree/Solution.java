package Trees.Serialize_and_Deserialize_Binary_Tree;

import java.util.Stack;

public class Solution {
        public class TreeNode {
            int val;
            TreeNode left;
            TreeNode right;
            TreeNode(int x) { val = x; }
        }
       int in = 0 ; 
       int n ; 
       String data ; 
       public String serialize(TreeNode root) {
           StringBuilder sb = new StringBuilder();
           Stack<TreeNode> stack = new Stack<>();
           stack.push(root);
           while (!stack.isEmpty()) {
               TreeNode curr = stack.pop();
               if (curr == null) {
                   sb.append("#");
               } else {
                   sb.append(curr.val).append(",");
                   stack.push(curr.right);
                   stack.push(curr.left);
               }
           }
           return sb.toString();
       }
   
       public TreeNode deserialize(String data) {
           if( data.length() == 0 ){
               return null ; 
           }
           this.n = data.length() ; 
           this.data = data ; 
           return helper() ; 
       }
   
       public TreeNode helper( ){
           if( data.charAt(in) == '#' ){
               return null ; 
           }
           boolean flag = false ; 
           if( data.charAt(in) == '-' ){
               flag = true; 
               in++ ; 
           }
           int val = 0 ; 
           while( in<n && data.charAt(in) != ',' ){
               val = val*10 + ( data.charAt(in) - '0' ) ;  
               in++ ; 
           }
           in++ ; 
           TreeNode root = new TreeNode( flag ? -val : val ) ;
           root.left = deserialize( data ) ;  
           in++ ; 
           root.right = deserialize( data ) ;  
           return root ; 
       }
   }
