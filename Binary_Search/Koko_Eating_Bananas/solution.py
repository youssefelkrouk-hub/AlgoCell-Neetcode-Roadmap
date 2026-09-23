class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1
        r = pow( 10 , 9 )
        while l < r : 
            mid = l + ( r-l )//2 
            time = 0 
            for i in piles : 
                time += ( i + mid -1 )//mid 
            if( time <= h ) : 
                r = mid 
            else : 
                l = mid + 1 

        return l 