class Solution {
    public:
        vector<vector<int>> subsets(vector<int>& nums) {
            vector<vector<int>> rs ; 
            int n = nums.size() ; 
            int len = 1 << n ; 
            for( int i=0 ; i<len ; ++i ){
                vector<int> curr ; 
                for( int j=0 ; j<n ; ++j ){
                    if( ( i & (1<<j) ) ){
                        curr.push_back( nums[j] ) ; 
                    }
                }
                rs.push_back( curr ) ; 
            }
            return rs ;
        }
    };