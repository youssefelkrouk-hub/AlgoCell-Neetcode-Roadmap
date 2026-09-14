class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort( nums ) ; 
        int n = nums.length ; 
        List<List<Integer>> rs = new ArrayList<>() ; 
        for( int i=0 ; i<n ; ++i ){
            if( nums[i] > 0 ) break ; 
            int l = i+1 ;
            int r = n-1 ; 
            int target = -nums[i] ; 
            while( l < r ){
                int sum = nums[l] + nums[r] ; 
                if( sum > target ){
                    r-- ; 
                }else if( sum < target ){
                    l++ ; 
                }else {
                    List<Integer> sol = new ArrayList<>() ; 
                    sol.add( nums[i] ) ;
                    sol.add( nums[l] ) ;
                    sol.add( nums[r] ) ;
                    rs.add( sol ) ;
                    while( l<r && nums[l+1] == nums[l] ) ++l ; 
                    ++l ; --r ; 
                }
            }
            while( i+1<n && nums[i+1] == nums[i] ){
                i++ ; 
            }
        }
        return rs ; 
    }
}