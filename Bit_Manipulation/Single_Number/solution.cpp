class Solution {
    public:
        int singleNumber(vector<int>& nums) {
            int rs = 0 ; 
            for( int i : nums ) {
                rs ^= i ; 
            }
            return rs ; 
        }
    };