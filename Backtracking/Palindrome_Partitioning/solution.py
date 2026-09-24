class Solution(object):
    def __init__(self) : 
        self.curr = [ ]
        self.rs = [ ]
    def isPal( self, s , l , r ) : 
        while l < r : 
            if s[l] != s[r] : 
                return False 
            l += 1 
            r -= 1 
        return True 
    def backtrack( self , s ,idx ) : 
        if( idx == len(s) ) :
            self.rs.append( list(self.curr) )
            return 
        for i in range( idx , len(s) ) : 
            if self.isPal( s , idx , i ) : 
                self.curr.append( s[idx:i+1] ) 
                self.backtrack( s , i+1 ) 
                self.curr.pop() 
    def partition(self, s):
        n = len(s) 
        self.backtrack( s , 0 ) 
        return self.rs 