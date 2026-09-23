class Solution(object):
    def minWindow(self, s, t):
        n = len(s)
        m = len(t) 
        if m > n : 
            return ""
        f = [0]*128
        count = 0 ; 
        for c in t : 
            f[ ord(c) ] += 1 
            if f[ ord(c) ] == 1 :
                count += 1 
        rs = -1 ; 
        start = 0 ; 
        length = n+m 

        for i in range(n) : 

            f[ ord( s[i] ) ] -= 1 
            if f[ ord( s[i] ) ] == 0 : 
                count -= 1 

            while start <= i and f[ ord( s[start] ) ] < 0 : 
                f[ ord( s[start] ) ] += 1 
                start += 1 
            
            if count == 0 and i - start + 1 < length : 
                rs = start 
                length = i - start + 1 


        if rs == -1 : 
            return ""
        else :
            return s[ rs : rs + length ] 