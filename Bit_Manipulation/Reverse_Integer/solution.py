class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  
        MAX = 2147483647  
        rev = 0 
        while x : 
            d = int( math.fmod( x , 10 ) )
            x = int( x / 10 )
            if rev > MAX//10 or ( rev == MAX//10 and d > MAX % 10 ) : 
                return 0 
            if rev < MIN//10 or ( rev == MIN//10 and d < MIN % 10 ) :
                return 0 
            rev = rev*10 + d 
        return rev