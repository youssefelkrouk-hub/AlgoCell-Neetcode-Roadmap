#include <string>
#include <stack>
using namespace std;

class Codec {
public:
    string serialize(TreeNode* root) {
        string res;
        stack<TreeNode*> stk;
        stk.push(root);
        while (!stk.empty()) {
            TreeNode* curr = stk.top();
            stk.pop();
            if (curr == nullptr) {
                res += "#";
            } else {
                res += to_string(curr->val) + ",";
                stk.push(curr->right);
                stk.push(curr->left);
            }
        }
        return res;
    }
    TreeNode* deserialize(string data) {
        int in = 0;
        return helper(data, in);
    }

    TreeNode* helper(const string& data, int& in) {
        if (data[in] == '#') {
            return nullptr;
        }
        bool flag = false;
        if (data[in] == '-') {
            flag = true;
            in++;
        }
        int val = 0;
        while (in < data.length() && data[in] != ',') {
            val = val * 10 + (data[in] - '0');
            in++;
        }
        in++; 
        TreeNode* root = new TreeNode(flag ? -val : val);
        root->left = helper(data, in) ; 
        in++;
        root->right = helper(data, in) ; 
        return root;
    }
};
