class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length ; 
        int rs = 0 ; 
        int max = prices[n-1] ; 
        for( int i=n-2 ; i>=0 ; --i ){ 
            if( prices[i] >= max ){
                max = prices[i] ; 
            }else {
                rs = Math.max( rs , max - prices[i] ) ; 
            }
        }
        return rs ;
    }
}