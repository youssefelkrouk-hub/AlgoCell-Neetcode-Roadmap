class Solution {
    public:
        int characterReplacement(string s, int k) {
            int n = s.size() ; 
            vector<bool> f(128) ; 
            for( char c : s ){
                f[c] = true ; 
            }
            int rs = 0 ; 
            for( int i=0 ; i<128 ; ++i ){
                if( !f[i] ) continue ; 
                int count = 0 ;
                int l = 0 ;  
                for( int j=0 ; j<n ; ++j ){
                    if( s[j] == i ) count++ ; 
                    while( j - l + 1 - count > k ){
                        if( s[l] == i ) count-- ; 
                        l++ ; 
                    }
                    rs = max( rs , j - l + 1 ) ; 
                }
            }
            return rs ;
        }
    };