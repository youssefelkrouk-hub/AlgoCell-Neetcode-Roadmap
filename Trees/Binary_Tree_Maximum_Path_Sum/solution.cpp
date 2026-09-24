
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
        int rs  ; 
        int helper( TreeNode* root ) {
            if( !root ){
                return 0 ; 
            }
            int curr = root->val ; 
            int maxLeft = max( 0 , helper( root->left ) ) ;  
            int maxRight = max( 0 , helper( root->right ) ) ;  
            rs = max( rs , curr + maxLeft + maxRight ) ; 
            return curr + max( maxLeft , maxRight ) ; 
        }
        int maxPathSum(TreeNode* root) {
            rs = root->val ; 
            helper( root ) ; 
            return rs ; 
        }
    };