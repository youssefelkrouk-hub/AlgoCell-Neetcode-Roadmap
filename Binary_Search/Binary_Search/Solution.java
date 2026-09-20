package Binary_Search.Binary_Search;

class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length ;  
        int l = 0 ; 
        int r = n -1 ; 
        while( l < r ){
            int mid = l + ( r - l )/2 ; 
            if( nums[mid] > target ){
                r = mid-1 ; 
            }else if( nums[mid] < target ) {
                l = mid + 1 ;
            }else {
                return mid ; 
            }
        }
        return nums[l] == target ? l : -1 ; 
    }
}