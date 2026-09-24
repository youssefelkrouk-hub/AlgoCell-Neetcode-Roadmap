
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
        string serialize(TreeNode* root) {
            if (root == nullptr) {
                return "$";
            }
            return "#" + to_string(root->val) + serialize(root->left) + serialize(root->right);
        }
    
        vector<int> get_ZArray(const string& s) {
            int n = s.size();
            vector<int> z(n, 0);
            int l = 0, r = 0;
            for (int i = 1; i < n; ++i) {
                if (i < r) {
                    z[i] = min(r - i, z[i - l]);
                }
                while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                    z[i]++;
                }
                if (i + z[i] > r) {
                    l = i;
                    r = i + z[i];
                }
            }
            return z;
        }
    
        bool isSubtree(TreeNode* root, TreeNode* subRoot) {
            string a = serialize(root);
            string b = serialize(subRoot);
            string rs = b + "-" + a;
            vector<int> z = get_ZArray(rs);
            int n = b.size();
            for (int i = n; i < rs.size(); ++i) {
                if (z[i] == n) {
                    return true;
                }
            }
            return false;
        }
    };