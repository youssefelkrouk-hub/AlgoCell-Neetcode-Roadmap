class Solution(object):
    def maxProfit(self, prices):
        n = len(prices) 
        rs = 0  
        m = prices[n-1] 
        for i in range(n-2,-1,-1) : 
            rs = max( rs , m - prices[i] )
            m = max(m , prices[i] )
        return rs  