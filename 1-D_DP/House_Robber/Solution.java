class Solution {
    public int rob(int[] nums) {
        int n = nums.length ; 
        if( n == 1 ) return nums[0] ; 
        int[] dp = new int[n+1] ; 
        dp[1] = nums[0] ;
        dp[2] = nums[1] ; 
        for( int i=3 ; i<=n ; ++i ){
            dp[i] = Math.max( dp[i-2] , dp[i-3] ) + nums[i-1] ; 
        }
        return Math.max( dp[n] , dp[n-1] ) ; 
    }
}