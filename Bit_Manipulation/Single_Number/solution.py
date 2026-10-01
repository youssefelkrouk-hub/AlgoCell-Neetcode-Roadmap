class Solution(object):
    def singleNumber(self, nums):
        rs = 0 
        for i in nums : 
            rs ^= i 
        return rs
        