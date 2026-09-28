class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1 : 
            return False 
        s = 0 
        for i in nums : 
            s += i 
        if s % 2 == 1 : 
            return False 
        dp = [False]*(( s//2 )+ 1 ) 
        dp[0] = True 
        for i in nums : 
            for j in range( (s//2) , i-1 , -1 ) : 
                dp[j] |= dp[j-i] 
        return dp[(s//2)]