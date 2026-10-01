class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length ; 
        int rs = n ; 
        for( int i=0 ; i<n ; ++i ){
            rs += ( i - nums[i] ) ; 
        }
        return rs ; 
    }
}