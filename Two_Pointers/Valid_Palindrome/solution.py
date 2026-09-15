class Solution(object):
    def isPalindrome(self, s):
        l = 0 
        r = len(s) - 1
        while l < r : 
            if not self.alphaNum( s[l] ) :
                l += 1 
                continue 
            if not self.alphaNum( s[r] ) : 
                r -= 1 
                continue 
            if s[l].lower() != s[r].lower() : 
                return False 
            l += 1 
            r -= 1 

        return True 

    def alphaNum( self , c ) : 
        return (( ord(c) >= ord('a') and ord(c) <= ord('z') ) or
            ( ord(c) >= ord('A') and ord(c) <= ord('Z') ) or
            ( ord(c) >= ord('0') and ord(c) <= ord('9') ) )
         