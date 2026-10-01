class Solution {
    public:
        bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
            bool a = false ; 
            bool b = false ; 
            bool c = false ;
            for( const auto &t : triplets ){
                if( t[0] == target[0] && t[1] <= target[1] && t[2] <= target[2] ){
                    a = true ; 
                }
                if( t[1] == target[1] && t[0] <= target[0] && t[2] <= target[2] ){
                    b = true ; 
                } 
                if( t[2] == target[2] && t[1] <= target[1] && t[0] <= target[0] ){
                    c = true ; 
                }
                if( a&&b&&c ) return true ; 
            } 
            return false ; 
        }
    };