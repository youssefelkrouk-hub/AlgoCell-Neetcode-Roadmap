class Solution {
    public:
        int coinChange(vector<int>& coins, int amount) {
            if( amount == 0 ) return 0 ; 
            vector<int> dp( amount+1 , 200'001 ) ; 
            dp[0] = 0 ; 
            for( int c : coins ){
                for( int j=c ; j<=amount ; ++j ){
                    dp[j] = min( dp[j] , dp[j-c] + 1 ) ; 
                }
            }
            return dp[amount]>amount ? -1 : dp[amount] ; 
        }
    };