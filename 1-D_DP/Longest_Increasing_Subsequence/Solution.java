import java.util.* ; 
class Solution {
    static class BIT {
        int[] bit ;
        int n ;  
        public BIT( int len ){
            n = len ; 
            bit = new int[len] ; 
        }
        int get(int idx){
            int rs = 0 ; 
            while( idx > 0 ){
                rs = Math.max( rs , bit[idx] ) ; 
                idx -= idx&-idx ;
            }
            return rs ;
        }
        void update( int idx , int val ){
            while( idx < n ){
                bit[idx] = Math.max( bit[idx] , val );
                idx += idx&-idx;
            }
        }
    }
    public int lengthOfLIS(int[] nums) {
        int n = nums.length ; 
        int[][] m = new int[n][2] ; 
        for( int i=0 ; i<n ; ++i ){
            m[i][0] = nums[i] ; 
            m[i][1] = i ; 
        }
        Arrays.sort( m , (a,b) -> a[0]-b[0] ) ; 
        int curr = 1; 
        for( int i=0 ; i<n ; ++i ){
            nums[m[i][1]] = curr; 
            while( i+1<n && m[i+1][0] == m[i][0] ){
                i++ ; 
                nums[m[i][1]]=curr;
            }
            curr++;
        }
        BIT bit = new BIT(curr) ;
        int lis = 0 ;  
        for( int i=0 ; i<n ; ++i ){
            int l = bit.get( nums[i]-1 )+1; 
            if(l>lis)lis=l;
            bit.update(nums[i],l) ; 
        }
        return lis ; 
    }
}