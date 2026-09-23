class Solution(object):
    def checkInclusion(self, s1, s2):
        n = len(s1) 
        m = len(s2) 
        f = [0]*128 
        for c in s1 : 
            f[ ord(c) ] += 1 
        l = 0  
        curr = [0]*128 
        length = 0 
        for i in range(m) : 
            length += 1 
            ind = ord( s2[i] )
            curr[ ind ] += 1 
            while curr[ ind ] > f[ ind ] : 
                length -= 1 
                curr[ ord( s2[l] ) ] -= 1 
                l += 1 
            if length == n :
                return True 
        return False
