

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
        void invert( TreeNode* root ){
            if( !root ){
                return ; 
            }
            TreeNode* temp = root->right ; 
            root->right = root->left ; 
            root->left = temp ; 
            invert( root -> right ) ; 
            invert( root -> left ) ; 
        }
        TreeNode* invertTree(TreeNode* root) {
            invert( root ) ; 
            return root ; 
        }
    };