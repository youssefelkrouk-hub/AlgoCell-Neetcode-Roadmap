class Solution(object):
    def helper( self , nums ) : 
        n = len( nums )
        dp = [0]*n 
        dp[0] = nums[0] 
        dp[1] = nums[1] 
        dp[2] = nums[0] + nums[2]
        for i in range( 3 , n ) : 
            dp[i] = nums[i] + max( dp[i-2] , dp[i-3] )
        return max( dp[n-2] , dp[n-1] )  

    def rob(self, nums):
        n = len( nums )
        if n <= 3 : 
            rs = 0 
            for i in nums : 
                rs = max( rs , i )
            return rs 
        elif n == 4 : 
            return max( nums[0] + nums[2] , nums[1] +  nums[3] )
        else :
            return max(self.helper(nums[1:]), self.helper(nums[:-1]))
