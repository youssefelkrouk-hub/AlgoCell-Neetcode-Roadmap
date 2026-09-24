package Trees.Subtree_of_Another_Tree;

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
   public String serialize( TreeNode root ){
       if( root == null ){
           return "$" ; 
       }
       return "#" + root.val + serialize( root.left ) + serialize( root.right ) ; 
   }
   public boolean isSubtree(TreeNode root, TreeNode subRoot) {
       String a = serialize( root ) ; 
       String b = serialize( subRoot ) ; 
       String rs = b + "-" + a ; 
       int[] arr = get_ZArray( rs ) ; 
       int n = b.length() ; 
       for( int i=n ; i<rs.length() ; ++i ){
           if( arr[i] == n ){
               return true ; 
           }
       }
       return false ; 
   }
   public int[] get_ZArray( String s ){
       int n = s.length() ; 
       int[] z = new int[n] ; 
       z[0] = 0 ;
       int l = 0 ; 
       int r = 0 ;  
       for( int i=1 ; i<n ; ++i ){
           if( i < r ){
               z[i] = Math.min( r - i , z[i-l] ) ;
           }
           while( z[i] + i < n && s.charAt( z[i] + i ) == s.charAt(z[i]) ){
               z[i]++ ; 
           }
           if( i + z[i] > r ){
               l = i ; 
               r = i + z[i] ; 
           }
       }
       return z ; 
   }
} 