class Solution {
    public:
        int search(vector<int>& nums, int target) {
            int n = nums.size() ; 
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
    };