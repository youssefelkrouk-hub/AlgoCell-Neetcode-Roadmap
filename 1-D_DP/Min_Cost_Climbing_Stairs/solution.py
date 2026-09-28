class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len( cost )
        a = cost[0]
        b = cost[1] 
        for i in range( 2 , n ) : 
            temp = a 
            a = b
            b = min( temp , b ) + cost[i]
        return min( a , b )