class Solution {
    public:
        void backtrack( int idx , vector<int> &nums , vector<int> &curr , vector<vector<int>> &rs  ){
            rs.push_back( vector<int>(curr) ) ; 
            for( int i=idx ; i<nums.size() ; ++i ){
                if( i>idx && nums[i-1] == nums[i] ) continue ; 
                curr.push_back( nums[i] ) ; 
                backtrack( i+1 , nums , curr , rs  ) ; 
                curr.pop_back() ;  
            }
        }
        vector<vector<int>> subsetsWithDup(vector<int>& nums) {
            sort( nums.begin() , nums.end() ) ; 
            vector<vector<int>> rs ; 
            vector<int> curr ; 
            backtrack( 0 , nums , curr , rs ) ; 
            return rs ; 
        }
    };