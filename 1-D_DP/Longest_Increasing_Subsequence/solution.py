class Solution(object):
    class BIT(object):
        def __init__(self,l) : 
            self.bit = [0]*l 
            self.n = l 
        def get(self,idx) : 
            rs = 0 
            while( idx > 0 ) :
                rs = max( rs , self.bit[idx] )
                idx -= idx&-idx
            return rs
        def update( self, idx , val ):
            while( idx < self.n ) : 
                self.bit[idx] = max( self.bit[idx] , val ) 
                idx += idx & -idx
        
    def lengthOfLIS(self, nums):
        n = len(nums) 
        m = [ [nums[i],i] for i in range(n)]
        m.sort()
        curr = 1
        i = 0 
        while i < n : 
            nums[ m[i][1] ] = curr 
            while i+1<n and m[i+1][0] == m[i][0] : 
                i += 1 
                nums[ m[i][1] ] = curr
            curr += 1
            i += 1 
        lis = 0 
        bit = self.BIT(curr)
        for i in range(n) : 
            l = bit.get(nums[i]-1)+1
            lis = max(lis,l)
            bit.update(nums[i],l)
        return lis