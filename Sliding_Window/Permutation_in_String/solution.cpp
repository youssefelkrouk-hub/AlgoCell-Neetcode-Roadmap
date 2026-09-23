class Solution {
    public:
        bool checkInclusion(string s1, string s2) {
            int n = s1.size() ; 
            int m = s2.size() ; 
            vector<int> f( 128 , 0 ) ; 
            for( char c : s1 ){
                f[ c ]++ ;
            }
            vector<int> curr( 128 , 0 ) ; 
            int len = 0 ; 
            int l = 0 ;
            for( int i=0 ; i<m ; ++i ){
                len++  ;
                curr[ s2[i] ]++ ; 
                while( curr[s2[i]] > f[s2[i]] ){
                    curr[s2[l]]-- ; 
                    l++ ; 
                    len-- ; 
                } 
                if( len == n ) return true ; 
            }
            return false ;  
        }
    };