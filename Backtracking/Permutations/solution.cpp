class Solution {
    public:
        vector<vector<int>> res ; 
        vector<vector<int>> permute(vector<int>& nums) {
            backtrack( 0 , nums ) ; 
            return res ; 
        }
        void backtrack( int idx , vector<int> &nums ){
            if( idx == nums.size() ){
                res.push_back( vector<int>(nums) ) ; 
            }
            for( int j=idx ; j<nums.size() ; ++j ){
                swap( nums[j] , nums[idx] ) ; 
                backtrack( idx+1,nums ) ; 
                swap( nums[j] , nums[idx] ) ; 
            }
        }
    };