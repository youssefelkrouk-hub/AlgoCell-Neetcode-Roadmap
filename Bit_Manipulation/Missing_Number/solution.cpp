class Solution {
    public:
        int missingNumber(vector<int>& nums) {
            int n = nums.size() ; 
            int rs = n ; 
            for( int i=0 ; i<n ; ++i ){
                rs += (  i - nums[i] ) ; 
            }
            return rs ; 
        }
    };