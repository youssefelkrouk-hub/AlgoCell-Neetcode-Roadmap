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
    int i = 0 ; 
    int p = 0 ; 
    TreeNode* helper( vector<int>& preorder, vector<int>& inorder , int val ){
        if( p >= preorder.size() ){
            return nullptr ; 
        }
        if( inorder[i] == val ){
            i++ ; 
            return nullptr ; 
        }
        TreeNode* root = new TreeNode( preorder[p++] ) ; 
        root->left = helper( preorder , inorder , root->val ) ; 
        root->right = helper( preorder , inorder , val ) ; 
        return root ; 
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper( preorder , inorder , INT_MIN ) ; 
    }
};