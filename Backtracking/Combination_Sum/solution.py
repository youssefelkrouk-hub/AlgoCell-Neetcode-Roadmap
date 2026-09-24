class Solution(object):
    def combinationSum(self, candidates, target):
        curr = [] 
        rs   = []
        self.backtrack( 0 , 0 , candidates , curr , rs , target )
        return rs
    def backtrack( self , val , i , candidates , curr , rs , target ) : 
        if val == target : 
            rs.append( list(curr) ) 
            return 
        for j in range( i , len( candidates ) ) :
            if val + candidates[j] <= target : 
                curr.append( candidates[j] ) 
                self.backtrack( val + candidates[j] , j , candidates , curr , rs , target )
                curr.pop()