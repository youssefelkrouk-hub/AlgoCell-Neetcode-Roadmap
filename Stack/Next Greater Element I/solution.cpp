class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> numsIndex1;
        for (int i = 0; i < nums1.size(); i++) {
            numsIndex1[nums1[i]] = i;
        }

        vector<int> res(nums1.size(), -1);
        stack<int> st;

        for (int i = 0; i < nums2.size(); i++) {
            int curr = nums2[i];
            while (!st.empty() && curr > st.top()) {
                int val = st.top();
                st.pop();
                int idx = numsIndex1[val];
                res[idx] = curr;
            }
            if (numsIndex1.find(curr) != numsIndex1.end()) {
                st.push(curr);
            }
        }

        return res;
    }
};