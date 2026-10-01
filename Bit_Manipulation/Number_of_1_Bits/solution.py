class Solution(object):
    def hammingWeight(self, n):
        rs = 0 
        while n > 0 : 
            n -= n & -n 
            rs += 1
        return rs 
        