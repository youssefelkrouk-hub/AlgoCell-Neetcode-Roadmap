class Solution(object):
    def subsets(self, nums):
        rs = [ ]
        n = len( nums ) 
        l = 1 << n 
        for i in range(l) : 
            curr = [] 
            for j in range(n) :
                if ( i & (1<<j) ) :
                    curr.append( nums[j] ) 
            rs.append(curr)
        return rs