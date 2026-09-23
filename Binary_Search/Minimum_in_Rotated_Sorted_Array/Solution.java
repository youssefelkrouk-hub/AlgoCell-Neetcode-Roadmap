package Binary_Search.Minimum_in_Rotated_Sorted_Array;

class Solution {
    public int findMin(int[] nums) {
        int n = nums.length ; 
        if( n == 1  ) return nums[0] ; 
        int l = 1 ;
        int r = n-1 ; 
        while( l < r ){
            int mid = l + ( r - l )/2 ; 
            if( nums[mid] > nums[0] ){
                l = mid + 1 ; 
            }else {
                r = mid ; 
            }
        } 
        return nums[l] < nums[0] ? nums[l] : nums[0] ; 
    }
}