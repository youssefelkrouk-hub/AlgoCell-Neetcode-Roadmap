import java.util.* ; 

public class Solution {
    public int coinChange(int[] coins, int amount) {
        if( amount == 0 ) return 0 ; 
        int[] dp = new int[amount+1] ; 
        Arrays.fill( dp , 200_000 ) ; 
        dp[0] = 0 ; 
        for( int c : coins ){
            for( int i=c ; i<=amount ; ++i ){
                dp[i] = Math.min( dp[i] , dp[i-c] + 1 ) ; 
            }
        }
        return dp[amount] > amount ? -1 : dp[amount] ; 
    }
}