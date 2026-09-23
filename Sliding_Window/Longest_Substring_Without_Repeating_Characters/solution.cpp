class Solution {
    public:
        int lengthOfLongestSubstring(string s) {
            int n = s.size() ; 
            vector<int> f( 128 , 0 ) ; 
            int rs = 0 ; 
            int start = 0 ; 
            for(int i=0 ; i<n ; ++i ){
                if( f[ s[i] ]++ == 1 ){
                    while( f[s[i]] > 1 ){
                        f[ s[start++] ]-- ; 
                    }
                }
                rs = max( rs , i - start + 1 ) ; 
            }
            return rs ; 
        }
    };