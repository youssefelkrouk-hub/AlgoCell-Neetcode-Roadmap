#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> rs(n - k + 1);
        deque<int> deq;
        int l = 0;

        for (int i = 0; i < n; ++i) {
            while (!deq.empty() && nums[deq.back()] <= nums[i]) {
                deq.pop_back();
            }

            deq.push_back(i);

            while (!deq.empty() && deq.front() < l) {
                deq.pop_front();
            }

            if (i >= k - 1) {
                rs[i - k + 1] = nums[deq.front()];
                l++;
            }
        }

        return rs;
    }
};
