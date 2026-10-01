class Solution(object):
    def partitionLabels(self, s):
        n = len(s)
        m = {} 
        for i in range( n ) :
            m[ s[i] ] = i 
        rs = []
        i = 0 
        while i < n:
            start = i 
            end = m[s[i]]
            while i < end :
                end = max( end , m[ s[i] ] ) 
                i += 1
            rs.append( end - start + 1 )
            i += 1
        return rs 