
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
        int isValid( TreeNode* root ){
            if( !root ){
                return 0 ; 
            }
            int a = isValid( root->left ) ; 
            int b = isValid( root->right ) ; 
            if( a != -1  && b!= -1 && abs( a - b ) <= 1 ){
                return max( a,b ) + 1 ; 
            }
            return -1 ; 
        }
        bool isBalanced(TreeNode* root) {
            if ( !root ){
                return true ; 
            }
            if( isValid( root ) != -1 ){
                return true ; 
            }
            return false ; 
        }
    };