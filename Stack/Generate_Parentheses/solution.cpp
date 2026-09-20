class Solution {
    public:
        vector<string> generateParenthesis(int n) {
            vector<vector<string>> dp(n+1) ; 
            dp[0].push_back("") ; 
            for( int i=1 ; i<=n ; ++i ){
                for( int j=0 ; j<i ; ++j ){
                    for( string a : dp[j] ){
                        for( string b : dp[i-j-1] ){
                            dp[i].push_back( "(" + a + ")" + b ) ;
                        }
                    }
                }
            }
            return dp[n] ; 
        }
    };