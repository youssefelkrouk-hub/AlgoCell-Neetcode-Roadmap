 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

class Solution {
public:
   int rs = 0 ; 
   int maxHeight( TreeNode* root ){
       if( !root ){
           return 0 ; 
       }
       int l = maxHeight( root->left ) ; 
       int r = maxHeight( root->right ) ; 
       rs = max( rs , r + l )  ;
       return max( l , r ) + 1 ;
   }
   int diameterOfBinaryTree(TreeNode* root) {
       maxHeight( root ) ; 
       return rs ; 
   }
};