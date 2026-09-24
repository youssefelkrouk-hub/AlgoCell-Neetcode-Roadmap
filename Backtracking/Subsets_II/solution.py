class Solution(object):
    def backtrack( self , idx , curr , nums , rs ) : 
        rs.append( list(curr) )
        for i in range( idx , len(nums) ) : 
            if i > idx and nums[i-1] == nums[i] :
                continue 
            curr.append( nums[i] )
            self.backtrack( i+1 , curr , nums , rs )
            curr.pop()

    def subsetsWithDup(self, nums):
        nums.sort() 
        rs = []
        self.backtrack( 0 , [] , nums , rs )
        return rs 