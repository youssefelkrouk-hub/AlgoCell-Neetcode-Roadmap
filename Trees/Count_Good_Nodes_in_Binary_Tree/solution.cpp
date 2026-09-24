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
        Solution() {
            std::ios_base::sync_with_stdio(false);
            std::cin.tie(nullptr);
            std::cout.tie(nullptr);
        }
        int rs = 0 ;  
        int goodNodes(TreeNode* root) {
            dfs( root , root->val ) ; 
            return rs ; 
        }
        void dfs( TreeNode* root , int curr ){
            if( !root ){
                return ; 
            }
            if( root->val >= curr ){
                rs++ ; 
                curr = max( curr , root->val ) ; 
            }
            dfs( root->left , curr ) ; 
            dfs( root->right , curr ) ; 
        }
    };