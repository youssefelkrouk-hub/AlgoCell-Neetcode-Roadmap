class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            int n = prices.size() ; 
            int rs = 0 ; 
            int m = prices[n-1] ; 
            for( int i=n-2 ; i>=0 ; --i ){ 
                if( prices[i] >= m ){
                    m = prices[i] ; 
                }else {
                    rs = max( rs , m - prices[i] ) ; 
                }
            }
            return rs ;
        }
    };