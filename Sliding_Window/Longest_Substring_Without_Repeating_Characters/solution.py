class Solution(object):
    def lengthOfLongestSubstring(self, s):
       f = [0]*128 
       rs = 0  
       start = 0  
       n = len(s) 
       for i in range(n) : 
            ind = ord( s[i] )
            f[ ord( s[i] ) ] += 1 
            while f[ ind ] > 1 : 
                f[ ord( s[start] ) ] -= 1 
                start += 1 
            rs = max( rs , i - start + 1 )
       return rs