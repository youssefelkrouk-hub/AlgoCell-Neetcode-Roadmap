class Solution {
    public int maxProduct(int[] nums) {
       int n = nums.length ; 
       int ans = nums[0] ; 
       int pref = 0 , suff = 0 ; 
       for( int i=0 ; i<n ; ++i ){
            pref = nums[i]*( pref==0 ? 1 : pref ) ; 
            suff = nums[n-1-i]*( suff == 0 ? 1 : suff ) ; 
            ans = Math.max( ans , Math.max( pref , suff ) ) ;    
       }
       return ans ;  
    }
}