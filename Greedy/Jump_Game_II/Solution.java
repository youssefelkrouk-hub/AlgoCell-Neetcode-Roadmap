class Solution {
    public int jump(int[] nums) {
        int n = nums.length ; 
        if( n == 1 ) return 0 ;  
        int limit = nums[0] ; 
        int next = 0 ; 
        int rs = 1 ; 
        for( int i=0 ; i<n ; ++i ){
            if( i <= limit ){
                if( i + nums[i] > next ){
                    next = i + nums[i] ; 
                }
            }else {
                rs++ ; 
                limit = next ; 
                next = i + nums[i] ; 
            }
        }  
        return rs ;
    }
}