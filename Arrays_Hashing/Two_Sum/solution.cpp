class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            int n = nums.size() ; 
            map<int,int> map ; 
            for( int i=0 ; i<n ; ++i ){
                int miss = target - nums[i] ; 
                if( map.count( miss ) ){
                    return { i , map[miss] } ; 
                }
                map[ nums[i] ] = i ; 
            }
            return {} ; 
        }
    };