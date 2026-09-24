import java.util.* ;

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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> rs = new ArrayList<>() ; 
        if( root == null ){
            return rs ; 
        }
        Queue<TreeNode> q = new LinkedList<>() ; 
        q.add( root ) ; 
        while( !q.isEmpty() ){
            int len = q.size() ; 
            TreeNode rightMost = null ; 
            while( len-- > 0 ){
                TreeNode curr = q.poll() ; 
                rightMost = curr ; 
                if( curr.left != null ){
                    q.add( curr.left ) ; 
                }
                if( curr.right != null ){
                    q.add( curr.right ) ; 
                }
            }
            rs.add( rightMost.val ) ; 
        }
        return rs;  
    }
}