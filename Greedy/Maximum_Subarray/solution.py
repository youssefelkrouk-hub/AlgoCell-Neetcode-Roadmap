class Solution(object):
    def maxSubArray(self, nums):
        n = len( nums ) 
        rs = nums[0] 
        curr = nums[0] 
        for i in range(1,n) : 
            curr = max( nums[i] , nums[i] + curr ) 
            rs = max( rs , curr )
        return rs 
        