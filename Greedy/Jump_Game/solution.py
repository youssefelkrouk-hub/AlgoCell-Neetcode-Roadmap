class Solution(object):
    def canJump(self, nums):
        n = len( nums )
        curr = nums[0] 
        for i in range( n ) : 
            if i > curr : 
                return False 
            curr = max( curr , i + nums[i] )
        return True 