class Solution {
    public:
        bool check( string &s , string &w , int ind ){
            for( int i=ind ; i<ind+w.size() ; ++i ){
                if( s[i] != w[i-ind] ) return false  ;
            }
            return true ; 
        }
        bool wordBreak(string s, vector<string>& wordDict) {
            int n = s.length() ; 
            vector<bool> dp( n+1 , false ) ; 
            dp[0] = true;  
            for( int i=0 ; i<n ; ++i ){
                if( dp[i] ){
                    for( string w : wordDict ){
                        if( i+w.size() <= n && check( s , w , i )){
                            dp[i+w.size()] = true ; 
                        }
                    }
                }
            } 
            return dp[n] ; 
        }
    };