class Solution(object):
    def missingNumber(self, nums):
        n = len(nums) 
        rs = n 
        for i in range(n) : 
            rs += i - nums[i]
        return rs 