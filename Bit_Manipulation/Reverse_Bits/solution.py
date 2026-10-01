class Solution(object):
    def countBits(self, n):
        rs = [0]*(n+1) 
        for i in range( 1 , n+1 ) : 
            if i & 1 : 
                rs[i] = 1 + rs[i-1] 
            else : 
                rs[i] = rs[i//2]
        return rs 