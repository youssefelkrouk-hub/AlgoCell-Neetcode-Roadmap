class Solution {
    public:
        vector<vector<int>> rs ;
        vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
            vector<int> curr ; 
            backtrack( 0 , 0 , candidates , curr , target ) ; 
            return rs ; 
        }
        void backtrack( int val , int i , vector<int> &candidates , vector<int> &curr , int target ){
            if( val == target ){
                rs.push_back( vector<int>( curr ) ) ; 
                return ;
            }
            for( int j=i ; j<candidates.size() ; ++j ){
                if( val + candidates[j] <= target ){
                    curr.push_back( candidates[j] ) ; 
                    backtrack( val + candidates[j] ,j , candidates , curr , target ) ; 
                    curr.pop_back( ); 
                }
            }
        }
    };