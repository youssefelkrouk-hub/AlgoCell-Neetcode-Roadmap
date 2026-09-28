class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 : 
            return 0  
        dp = [200_001]*( amount + 1 )
        dp[0] = 0 
        for c in coins : 
            for j in range( c , amount+1 ) : 
                dp[j] = min( dp[j] , dp[j-c] + 1 )

        if dp[amount] > amount : 
            return -1  
        else :
            return dp[amount]