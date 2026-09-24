import java.util.* ; 
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length ; 
        int len = 1 << n ; 
        List<List<Integer>> rs = new ArrayList<>() ;
        for( int i=0 ; i<len ; ++i ){
            List<Integer> curr = new ArrayList<>() ; 
            for( int j=0 ; j<n ; ++j ){
                if( (i & ( 1 << j )) != 0 ){
                    curr.add( nums[j] ) ; 
                }
            }
            rs.add( curr ) ; 
        }       
        return rs ;
    }
}