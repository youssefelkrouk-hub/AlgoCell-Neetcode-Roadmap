package Trees.Construct_Binary_Tree_From_Preorder_And_Inorder_Traversal;


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
    int i=0 ; 
    int p=0 ; 
    public TreeNode helper(int[] preorder, int[] inorder, int val ) {
        if( p >= preorder.length ){
            return null ; 
        }
        if( inorder[i] == val ){
            ++i ; 
            return null ; 
        }
        TreeNode root = new TreeNode( preorder[p++] ) ; 
        root.left = helper( preorder , inorder , root.val ) ; 
        root.right = helper( preorder , inorder, val ) ; 
        return root ; 
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper(preorder, inorder, Integer.MIN_VALUE );
    }
}
