class Solution {
    public:
        vector<int> countBits(int n) {
            vector<int> rs(n+1) ; 
            for( int i=1 ; i<=n ; ++i ){
                if( i & 1 ){
                    rs[i] = 1 + rs[i-1] ; 
                }else {
                    rs[i] = rs[i/2] ; 
                }
            }
            return rs ;
        }
    };