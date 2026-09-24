
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
        vector<int> rightSideView(TreeNode* root) {
            vector<int> rs ; 
            if ( !root ){
                return rs ; 
            }
            queue<TreeNode*> q ; 
            q.push( root ) ; 
            while( !q.empty() ){
                int len = q.size() ; 
                int val = -1 ; 
                while( len-- ){
                    TreeNode* curr = q.front() ; 
                    q.pop() ;    
                    val = curr->val ; 
                    if( curr->left ){
                        q.push( curr->left ) ; 
                    }
                    if( curr->right ){
                        q.push( curr->right ) ; 
                    }
                }
                rs.push_back( val ) ; 
            }
            return rs ; 
        }
    };