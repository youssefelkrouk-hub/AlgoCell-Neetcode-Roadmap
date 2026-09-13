from collections import defaultdict

class Solution(object):
    def longestConsecutive(self, nums):
        m = defaultdict(int)
        rs = 0  
        for i in nums : 
            if not m[i] : 
                len = 1 + m[i-1] + m[i+1] 
                m[i] = len 
                m[ i - m[i-1] ] = len 
                m[ i + m[i+1] ] = len 
                rs = max( rs , len )
        return rs 