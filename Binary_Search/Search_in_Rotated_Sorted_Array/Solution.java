package Binary_Search.Search_in_Rotated_Sorted_Array;

class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length ; 
        int l = 0 ; 
        int r = n-1 ; 
        while( l < r ){
            int mid = l + ( r - l )/2 ; 
            if( nums[mid] < nums[r] ){
                r = mid ; 
            }else {
                l = mid + 1 ; 
            }
        }
        r = l + n-1  ; 
        while( l < r ){
            int mid = l + ( r - l )/2 ; 
            if( nums[mid%n] > target ){
                r = mid -1 ; 
            }else if( nums[mid%n] < target ){
                l = mid +1 ; 
            }else {
                return mid%n ; 
            }
        }
        l %= n ; 
        return nums[l] == target ? l : -1 ; 
    }
}

// A Better Solution ( using 1 pass Binary Search )

// class Solution {
//     public int search(int[] nums, int target) {
//         int n = nums.length ; 
//         int l = 0 ; 
//         int r = n-1 ; 
//         while( l < r ){
//             int mid = l + ( r-l )/2 ; 
//             if( nums[l] <= target ){
//                 if( nums[mid] < nums[l] ){
//                     r = mid - 1 ; 
//                 }else if( nums[mid] >= target ){
//                     r = mid ; 
//                 }else {
//                     l = mid + 1 ;
//                 }
//             }else if( nums[r] >= target ) {
//                 if( nums[mid] >= nums[l] ){ 
//                     l = mid + 1 ; 
//                 }else if( nums[mid] >= target ){
//                     r = mid ; 
//                 }else {
//                     l = mid + 1 ; 
//                 }
//             }else {
//                 break ; 
//             }
//         }
//         return nums[l] == target ? l : -1 ; 
//     }
// }