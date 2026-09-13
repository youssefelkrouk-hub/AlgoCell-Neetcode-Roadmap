import java.util.HashMap; 
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length ; 
        HashMap<Integer,Integer> map = new HashMap<>() ; 
        for( int i=0 ; i<n ; ++i ){
            int miss = target - nums[i] ; 
            if( map.get(miss) != null ){
                return new int[]{ map.get(miss) , i } ; 
            }
            map.put( nums[i] , i ) ; 
        }
        return new int[0] ; 
    }
}   
