class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s) 
        rs = 0 
        f = [True]*128
        for c in s : 
            f[ ord(c) ] = False
        for i in range(128) : 
            if f[i] :
                continue 
            l = 0 
            count = 0 
            for j in range(n) : 
                if ord( s[j] ) == i : 
                    count += 1 
                while j - l + 1 - count > k : 
                    if ord( s[l] ) == i : 
                        count -= 1 
                    l += 1 
                rs = max( rs , j - l + 1 ) 

        return rs  
        