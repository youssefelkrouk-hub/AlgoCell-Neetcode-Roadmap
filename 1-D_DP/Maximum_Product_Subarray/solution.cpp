class Solution {
    public:
        int maxProduct(vector<int>& nums) {
            int n = nums.size() ; 
            int ans = nums[0] ; 
            int pref = 0 , suff = 0 ; 
            for( int i=0 ; i<n ; ++i ){
                pref = nums[i]*( pref != 0 ? pref : 1 ) ; 
                suff = nums[n-1-i]*( suff !=0 ? suff : 1 ) ; 
                ans = max( ans , max( pref , suff ) ) ; 
            }
            return ans ; 
        }
    };