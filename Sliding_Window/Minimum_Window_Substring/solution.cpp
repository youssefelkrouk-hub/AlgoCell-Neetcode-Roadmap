class Solution {
    public:
        string minWindow(string s, string t) {
            int n = s.size() ; 
            int m = s.size() ; 
            if( m > n ){
                return "" ; 
            }
            vector<int> f( 128 , 0 ) ; 
            int count = 0 ; 
            for( char c : t){
                if( f[c]++ == 0 ) count++ ; 
            } 
            int rs = -1 ; 
            int start = 0 ; 
            int len = INT_MAX ; 
            for( int i=0 ; i<n ; ++i ){
                if( --f[ s[i] ] == 0  ){
                    count-- ; 
                }
                while( start<=i && f[ s[start] ] < 0 ){
                    f[ s[start++] ]++ ;  
                }
                if( count == 0 && i - start + 1 < len ){
                    rs = start ; 
                    len = i - start + 1 ;
                }
            }
            return rs == -1 ? "" : s.substr( rs , len ) ; 
        }
    };