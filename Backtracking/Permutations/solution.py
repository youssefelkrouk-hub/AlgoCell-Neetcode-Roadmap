class Solution(object):
    def backtrack( self , idx , nums , rs ) :
        if idx == len( nums ) :
            rs.append( list(nums) )
        for j in range( idx , len(nums) ) : 
            nums[j] , nums[idx] = nums[idx] , nums[j]
            self.backtrack( idx+1 , nums , rs )
            nums[j] , nums[idx] = nums[idx] , nums[j]

    def permute(self, nums):
        rs = []
        self.backtrack( 0 , nums , rs ) 
        return rs        