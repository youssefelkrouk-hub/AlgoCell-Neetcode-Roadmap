class Solution {
    public int trap(int[] height) {
        int n = height.length ; 
        if( n <= 2 ){
            return 0 ; 
        }
        int rs = 0 ; 
        int r = n-1 ; 
        int l = 0 ; 
        int leftMax = height[0] ; 
        int rightMax = height[n-1] ; 
        while( l < r ){
            if( leftMax < rightMax ){
                l++ ; 
                leftMax = Math.max( leftMax , height[l] ) ; 
                rs += leftMax - height[l] ; 
            }else {
                r-- ;
                rightMax = Math.max( rightMax , height[r] ) ; 
                rs += rightMax - height[r] ; 
            }
        }
        return rs ; 
    }
}