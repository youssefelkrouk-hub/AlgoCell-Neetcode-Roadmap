class Solution {
    public int helper( int start , int end , int[] nums ){
        int n = nums.length ; 
        int[] dp = new int[n] ; 
        dp[start] = nums[start] ; 
        dp[start+1] = nums[start+1] ; 
        dp[start+2] = nums[start] + nums[start+2] ; 
        for( int i=start+3 ; i<=end ; ++i ){
            dp[i] = nums[i] + Math.max( dp[i-2] , dp[i-3] ) ;  
        } 
        return Math.max( dp[end-1] , dp[end] ) ; 
    }
    public int rob(int[] nums) {
        int n = nums.length ; 
        if( n <= 3 ){
            int rs = 0 ; 
            for( int i : nums ){
                rs = Math.max( rs , i ) ; 
            } 
            return rs ; 
        }else if( n == 4 ){
            return Math.max( nums[0] + nums[2] , nums[1] + nums[3] ) ;  
        }
        return Math.max( helper( 0,n-2,nums ) , helper( 1 ,n-1 , nums ) ) ; 
    }
}