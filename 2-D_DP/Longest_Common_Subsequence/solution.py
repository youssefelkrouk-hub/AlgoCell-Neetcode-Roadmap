class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        if len(text1) < len(text2) : 
            text1 , text2 = text2 , text1
        n = len(text1)
        m = len(text2)
        dp = [0]*(m+1) 
        for i in range(n-1,-1,-1) : 
            prev = 0 
            for j in range( m-1,-1,-1 ) :
                temp = dp[j]
                if text1[i] ==  text2[j] :
                    dp[j] = 1 + prev 
                else : 
                    dp[j] = max( dp[j] , dp[j+1] )
                prev = temp 
        return dp[0] 