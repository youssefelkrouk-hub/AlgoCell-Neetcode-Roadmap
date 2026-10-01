class Solution {
    public:
        int longestCommonSubsequence(string text1, string text2) {
            if( text1.size() < text2.size() ){
                swap( text1 , text2 ) ; 
            }
            int n = text1.size() ; 
            int m = text2.size() ; 
            vector<int> dp( m+1 , 0 ) ; 
            for( int i=n-1 ; i>=0 ; --i ){
                int next = 0; 
                for( int j=m-1 ; j>=0 ; --j ){
                    int temp = dp[j] ; 
                    if( text1[i] == text2[j] ){
                        dp[j] = 1 + next ; 
                    }else {
                        dp[j] = max( dp[j] , dp[j+1] ) ; 
                    }
                    next = temp ; 
                }
            }
            return dp[0] ; 
        }
    };