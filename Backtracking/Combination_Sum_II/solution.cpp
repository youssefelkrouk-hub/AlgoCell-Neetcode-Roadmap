class Solution {
    public:
        vector<vector<int>> rs ; 
        vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
            sort( candidates.begin() , candidates.end() ) ; 
            vector<int> curr ; 
            backtrack( 0 , 0 , curr , candidates , target ) ; 
            return rs ;
        }
        void backtrack( int val , int i , vector<int> &curr , vector<int> &candidates , int target ){
            if( val == target ){
                rs.push_back( vector<int>(curr) ) ; 
                return ; 
            }
            if( i == candidates.size() ) return ; 
            if( val + candidates[i] <= target ){
                curr.push_back( candidates[i] ) ; 
                backtrack( val + candidates[i] , i+1 , curr ,  candidates,  target ) ; 
                curr.pop_back() ; 
            }   
            while( i+1 < candidates.size() && candidates[i+1] == candidates[i] ){
                i++ ; 
            }
            backtrack( val , i+1 , curr ,  candidates , target ) ; 
        }
    };