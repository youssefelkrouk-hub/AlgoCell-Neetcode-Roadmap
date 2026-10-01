package Greedy.Jump_Game;

class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length ; 
        int curr = 0 ; 
        for( int i=0 ; i<n ; ++i ){
            if( curr < i ) return false ; 
            curr = Math.max( curr , i + nums[i] ) ;  
        }
        return true ;
    }
}