import java.util.* ; 

class Solution {
    public boolean canPartition(int[] nums) {
        int n = nums.length ; 
        if( n == 1 ) return false ; 
        int sum = 0 ; 
        for( int i : nums ) sum += i ; 
        if( sum % 2 == 1 ) return false ; 
        boolean[] dp = new boolean[sum/2+1] ; 
        dp[0] = true ; 
        for( int i : nums ){
            for( int j=sum/2 ; j>=i ; --j ){
                dp[j] |= dp[j-i] ; 
            }
        }
        return dp[sum/2] ;
    }
}